# ☕ Dashboard de Operaciones - Cafetería UNAHUR

Este proyecto es una aplicación interactiva de **Business Intelligence y Data Science** diseñada para analizar y optimizar las operaciones de la cafetería universitaria.

La herramienta integra análisis descriptivo, series temporales y modelos predictivos para ayudar a la gerencia en la toma de decisiones basada en datos.

## 🚀 Funcionalidades Principales

La aplicación está dividida en 4 módulos estratégicos:

1.  **Business Intelligence (KPIs):**
    * Análisis de ingresos totales y ticket promedio.
    * Comparativa de rendimiento entre sedes (Boxplots interactivos) para detectar variabilidad operativa.
    * Análisis de correlaciones: ¿Influye el tiempo de espera en la satisfacción?

2.  **Tendencias Temporales:**
    * Visualización de la evolución histórica de visitas.
    * Detección de estacionalidad (picos de fin de año y valles de receso).

3.  **Simulador de Tiempos de Espera (Regresión):**
    * Modelo predictivo ($Tiempo = -0.21 + 2.07 \times Cantidad$) que estima la demora según el tamaño del pedido.
    * Sistema de alertas para pedidos grandes (>12 unidades) donde el modelo lineal pierde precisión.

4.  **Laboratorio de Datos (Imputación):**
    * Módulo técnico que demuestra técnicas de limpieza de datos.
    * Comparación en tiempo real entre datos originales vs. imputación con KNN para corregir registros faltantes en pedidos de 3 unidades.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Framework Web:** Streamlit
* **Visualización:** Plotly Express
* **Manipulación de Datos:** Pandas, NumPy

## 📂 Estructura del Proyecto

    ├── app.py              # Código principal de la aplicación
    ├── requirements.txt    # Dependencias del proyecto
    ├── data/               # Datasets procesados (CSV)
    └── README.md           # Documentación

## 📦 Instalación y Uso Local

1.  Clonar el repositorio:

        git clone [https://github.com/TU_USUARIO/dashboard-cafeteria-unahur.git](https://github.com/TU_USUARIO/dashboard-cafeteria-unahur.git)

2.  Instalar dependencias:

        pip install -r requirements.txt

3.  Ejecutar la aplicación:

        streamlit run app.py

---
*Proyecto académico para la asignatura de Fundamentos de Ciencias de Datos - Tecnicatura Universitaria en IA (UNAHUR).*