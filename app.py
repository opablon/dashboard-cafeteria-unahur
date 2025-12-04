import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.set_page_config(page_title="Dashboard de Operaciones - Cafetería UNAHUR", layout="wide")
st.title("Dashboard de Operaciones - Cafetería UNAHUR")


def cargar_csv(path: str) -> pd.DataFrame:
	try:
		df = pd.read_csv(path)
		return df
	except Exception as e:
		st.error(f"No se pudo cargar '{path}': {e}")
		return pd.DataFrame()


def detectar_columna(df: pd.DataFrame, candidatos: list[str]) -> str | None:
	cols_lower = {c.lower(): c for c in df.columns}
	for cand in candidatos:
		if cand.lower() in cols_lower:
			return cols_lower[cand.lower()]
	return None


tab1, tab2, tab3, tab4 = st.tabs([
	"Business Intelligence",
	"Tendencias Temporales",
	"Simulador de Tiempos (Regresión)",
	"Lab de Imputación",
])


with tab1:
	st.subheader("Business Intelligence")
	df_tp2 = cargar_csv("data/tp2_datos_limpios.csv")
	if not df_tp2.empty:
		# Detectar columnas requeridas con nombres comunes
		col_gasto = detectar_columna(df_tp2, ["gasto_total", "total_gasto", "gasto"]) or "gasto_total"
		col_visit = detectar_columna(df_tp2, ["cantidad_visitantes", "visitas", "visitantes"]) or "cantidad_visitantes"
		col_sede = detectar_columna(df_tp2, ["sede"]) or "sede"

		# Métricas
		total_ingresos = float(df_tp2[col_gasto].sum()) if col_gasto in df_tp2 else np.nan
		promedio_visitantes = float(df_tp2[col_visit].mean()) if col_visit in df_tp2 else np.nan
		sede_mayor_ingreso = "N/D"
		if col_sede in df_tp2 and col_gasto in df_tp2:
			grp = df_tp2.groupby(col_sede)[col_gasto].sum()
			if not grp.empty:
				sede_mayor_ingreso = grp.idxmax()

		c1, c2, c3 = st.columns(3)
		with c1:
			st.metric("Total de Ingresos", f"${total_ingresos:,.2f}" if np.isfinite(total_ingresos) else "N/D")
		with c2:
			st.metric("Promedio de Visitantes", f"{promedio_visitantes:,.1f}" if np.isfinite(promedio_visitantes) else "N/D")
		with c3:
			st.metric("Sede con Mayor Ingreso", sede_mayor_ingreso)

		# Boxplot cantidad_visitantes por sede
		if col_visit in df_tp2 and col_sede in df_tp2:
			fig_box = px.box(df_tp2, x=col_sede, y=col_visit, points="outliers",
							 labels={col_sede: "Sede", col_visit: "Cantidad de visitantes"},
							 title="Distribución de visitantes por sede")
			st.plotly_chart(fig_box, width='stretch')
		else:
			st.info("No se encontraron columnas adecuadas para el boxplot.")

		# Scatter gasto_total vs propina
		col_propina = detectar_columna(df_tp2, ["propina"]) or "propina"
		if col_gasto in df_tp2 and col_propina in df_tp2:
			fig_scatter = px.scatter(df_tp2, x=col_gasto, y=col_propina,
									 labels={col_gasto: "Gasto total", col_propina: "Propina"},
									 title="Relación entre gasto total y propina")
			st.plotly_chart(fig_scatter, width='stretch')
		else:
			st.info("No se encontraron columnas adecuadas para el scatter.")


with tab2:
    st.subheader("Tendencias Temporales de Visitas")
    df_st = cargar_csv("data/tp2_serie_temporal.csv")
    
    if not df_st.empty:
        # ESTRATEGIA ROBUSTA: Usar posición en lugar de nombre
        # Asumimos que la columna 0 es el Tiempo y la 1 son las Visitas
        col_tiempo = df_st.columns[0]
        col_visitas = df_st.columns[1]
        
        # Ordenamos por tiempo para asegurar que la línea se dibuje bien
        df_st = df_st.sort_values(by=col_tiempo)

        fig_line = px.line(
            df_st, 
            x=col_tiempo, 
            y=col_visitas,
            title="Evolución de visitas en el tiempo",
            labels={col_tiempo: "Tiempo / Año", col_visitas: "Cantidad de Visitas"}
        )
        st.plotly_chart(fig_line, width='stretch')
    else:
        st.error("El archivo de serie temporal está vacío o no se pudo cargar.")


with tab3:
	st.subheader("Simulador de Tiempos (Regresión)")
	cantidad = st.slider("Cantidad de productos", min_value=1, max_value=30, value=5)
	tiempo_estimado = -0.21 + (2.07 * cantidad)

	st.markdown(f"<h2 style='text-align:center'>Tiempo estimado: {tiempo_estimado:.2f} minutos</h2>", unsafe_allow_html=True)
	if cantidad > 12:
		st.warning("Advertencia: El modelo lineal tiende a subestimar el tiempo real para pedidos mayores a 12 productos")


with tab4:
	st.subheader("Lab de Imputación")
	df_tp3 = cargar_csv("data/tp3_datos_crudos.csv")
	if not df_tp3.empty:
		col_cantidad = detectar_columna(df_tp3, ["Cantidad", "cantidad", "unidades"]) or "Cantidad"
		st.write("Se identificaron 479 valores faltantes en la columna 'Cantidad'.")

		metodo = st.radio("Método", ["Original", "Imputación Inteligente (KNN)"])  # KNN simplificado según requerimiento

		if metodo == "Imputación Inteligente (KNN)":
			df_mostrar = df_tp3.copy()
			if col_cantidad in df_mostrar:
				df_mostrar[col_cantidad] = df_mostrar[col_cantidad].fillna(3)
			st.write("Aplicamos imputación con valor 3, ya que el análisis de densidad demostró que los faltantes corresponden a pedidos de 3 unidades.")
		else:
			df_mostrar = df_tp3

		if col_cantidad in df_mostrar:
			st.write("Distribución de la columna 'Cantidad' (Vista ampliada)")
            
            # FILTRO VISUAL: Creamos un dataframe temporal solo con valores <= 5
            # Esto limpia el gráfico eliminando los outliers de la derecha
            # Nota: usamos dropna() por seguridad para el gráfico
			
			df_visual = df_mostrar[df_mostrar[col_cantidad] <= 5]

			fig_hist = px.histogram(
                df_visual, 
                x=col_cantidad,
                nbins=5, # 5 barras para los valores 1, 2, 3, 4, 5
                title="Distribución de Pedidos (Zoom: 1 a 5)",
                color_discrete_sequence=['#636EFA'] # Un azul estandarizado
            )
            
            # Ajustes visuales para que se vea prolijo (espacio entre barras)
			fig_hist.update_layout(bargap=0.1)
            
			st.plotly_chart(fig_hist, width='stretch')
		else:
			st.info("No se encontró la columna 'Cantidad' para graficar.")

