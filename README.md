# Proyecto Machine Learning: Predicción de Demanda
Este repositorio contiene un proyecto integral de Machine Learning para la predicción de la demanda diaria de productos por departamento, utilizando un conjunto de datos de cadena de suministro. El objetivo principal es optimizar la gestión de inventario y la planificación logística a través de predicciones precisas.

## Descripción del Proyecto

El proyecto se centra en construir y evaluar modelos de regresión supervisada para estimar la cantidad de productos vendidos por departamento cada día. Se explora el impacto de diversas variables clave y se proporciona una demo interactiva para simular predicciones.

## Origen de Datos

Se utiliza el **DataCoSupplyChainDataset**, que abarca ventas, pedidos y beneficios desde 2015 hasta 2018. Este dataset contiene más de 1,000,000 de observaciones y variables cruciales para la cadena de suministro.

## Objetivo del Modelo

Estimar la **demanda diaria** (cantidad de productos vendidos) para cada departamento, mejorando la planificación operativa y la toma de decisiones estratégicas.

## Procesamiento de Datos y Feature Engineering

El pipeline de procesamiento incluye:
1.  **Limpieza y Preparación:** Eliminación de valores nulos y duplicados.
2.  **Variables Temporales:** Creación de variables como año, mes y día de la semana para capturar patrones estacionales y diarios.
3.  **Codificación Categórica:** Uso de One-Hot Encoding para variables como 'Department Name'.
4.  **Escalado Numérico:** Normalización de variables numéricas para optimizar el rendimiento del modelo.

## Modelos Probados y Evaluación

Se evaluaron tres modelos de regresión supervisada con una división train/test de 80/20:
* **Random Forest:** Modelo de ensamblaje robusto basado en múltiples árboles de decisión.
* **XGBoost:** Algoritmo de gradient boosting conocido por su alta precisión y eficiencia.
* **LightGBM:** Framework de gradient boosting de alto rendimiento, optimizado para grandes datasets.

Las métricas de evaluación utilizadas son:
* **R² (Coeficiente de Determinación):** Mide la proporción de la varianza en la variable dependiente que es predecible a partir de las variables independientes.
* **RMSE (Error Cuadrático Medio):** Mide la magnitud promedio de los errores del modelo.
* **MAE (Error Absoluto Medio):** Mide la magnitud promedio de los errores en un conjunto de predicciones, sin considerar su dirección.

### Resultados Clave:
**XGBoost:** Demostró el mejor R² con un valor de **0.85**, indicando un alto poder explicativo[cite: 3].
**Random Forest:** Tuvo el mejor RMSE con **4.63** y MAE con **2.07**[cite: 1].

## Variables Más Relevantes

Se identificaron las siguientes variables con mayor influencia en la predicción de la demanda diaria:
**Ventas Totales:** El factor más influyente en la estimación de la demanda[cite: 2].
**Ganancia por Orden:** Impacta directamente en la cantidad de productos demandados[cite: 2].
**Departamento:** La categoría del departamento influye significativamente en la demanda[cite: 2].
**Variables Temporales (Día de la semana y Mes):** Revelan patrones de demanda estacionales y diarios[cite: 2].

## Demo Interactiva en Streamlit

Se ha desarrollado un dashboard interactivo en Streamlit (`app.py`) para:
* **Visualización y Comparación:** Explorar modelos, métricas y resultados de manera intuitiva.
* **Simulador Predictivo:** Obtener predicciones de demanda en tiempo real al ingresar parámetros propios.

## Estructura del Proyecto