---
title: Dashboard Cafeteria Unahur
emoji: ☕
colorFrom: gray
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
---

# ☕ Dashboard de Operaciones - Cafetería UNAHUR

Este proyecto es una aplicación **Full-Stack de Data Science** diseñada para optimizar las operaciones de una cafetería universitaria. Transforma un análisis académico estático en un **Dashboard Interactivo de Gestión**.

La herramienta integra Business Intelligence, series temporales con IA (Prophet) y simuladores predictivos para la toma de decisiones basada en datos.

## 🚀 Funcionalidades Principales

La aplicación cuenta con 5 módulos estratégicos:

1.  **Business Intelligence (KPIs):**
    * Tablero de control con ingresos y métricas de afluencia.
    * **Análisis de Correlaciones:** Mapa de calor (Heatmap) que valida la relación crítica entre Tiempos de Espera y Satisfacción del Cliente.
    * Filtros dinámicos por Sede.

2.  **Forecasting con IA (Prophet):**
    * Modelo de aprendizaje automático (Meta Prophet) para la predicción de demanda.
    * Detección automática de estacionalidad académica (recesos vs. exámenes).
    * Proyección interactiva a 3 meses.

3.  **Simulador de Tiempos (Regresión Lineal):**
    * Modelo predictivo ($Tiempo = -0.21 + 2.07 \times Cantidad$) para estimar demoras en cocina.
    * **Calculadora de Riesgo:** Alertas automáticas de satisfacción según el tiempo proyectado.

4.  **Laboratorio de Datos (Data Quality):**
    * Módulo técnico de limpieza de datos.
    * Demostración de imputación con **KNN (K-Nearest Neighbors)** para recuperar información perdida de pedidos específicos.

5.  **Conclusiones Estratégicas:**
    * Reporte ejecutivo automatizado con hallazgos de negocio y recomendaciones operativas.

## 🛠️ Tecnologías Utilizadas

* **Core:** Python 3.10+, Streamlit.
* **Machine Learning:** Prophet (Forecasting), Scikit-learn.
* **Visualización:** Plotly Express (Gráficos interactivos adaptados a Dark Mode).
* **ETL & Análisis Previo:** R / RStudio (Scripts disponibles en `/r_scripts`).

## 📂 Estructura del Proyecto

    ├── app.py              # Aplicación principal
    ├── requirements.txt    # Dependencias (incluye Prophet)
    ├── data/               # Datasets procesados (CSV)
    ├── r_scripts/          # ETL original y análisis exploratorio en R
    └── README.md           # Documentación

## 📦 Instalación Local

1.  Clonar el repositorio:

        git clone https://github.com/opablon/dashboard-cafeteria-unahur

2.  Instalar dependencias:

        pip install -r requirements.txt

3.  Ejecutar la aplicación:

        streamlit run app.py

---
*Proyecto basado en trabajos académicos para la asignatura Fundamentos de Ciencias de Datos de la Tecnicatura Universitaria en IA (UNAHUR).*