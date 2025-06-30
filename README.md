
# 📦 Supply Chain Demand Prediction

Predicción de la demanda diaria por departamento en una cadena de suministro utilizando algoritmos de machine learning como **Random Forest**, **XGBoost** y **Regresión Lineal**, con análisis de resultados, visualizaciones y una app interactiva en **Streamlit**.

---

## 📁 Dataset

El dataset proviene de **DataCo Supply Chain Dataset**, que incluye información sobre ventas, clientes, productos y beneficios diarios.

---

## 🎯 Objetivo del proyecto

- Predecir la cantidad de productos vendidos por día y por departamento.
- Comparar el rendimiento de diferentes modelos de regresión.
- Visualizar resultados y permitir predicciones interactivas a través de una interfaz Streamlit.

---

## 🔧 Preprocesamiento

- Limpieza de datos: selección de columnas clave, conversión de fechas y tratamiento de valores nulos.
- Agrupación por día y departamento para obtener ventas, cantidad y beneficios.
- Ingeniería de features: codificación one-hot de departamentos y extracción de información temporal (año, mes, día de la semana).
- Escalado de variables numéricas con `StandardScaler`.

---

## 🧠 Modelos entrenados

Se evaluaron tres modelos principales:

| Modelo            | R² (CrossVal) | RMSE (Test) | MAE (Test) |
|------------------|---------------|-------------|------------|
| Random Forest     | 0.9849        | 4.63        | 2.07       |
| XGBoost           | 0.9858        | 4.68        | 2.11       |
| LightGBM          | 0.9817        | 4.85        | 2.20       |
| Linear Regression | ~0.78         | >8.00       | >4.00      |


✅ **Mejor modelo:** `Random Forest`, seguido muy de cerca por `XGBoost`.

---

## 📊 Visualización de resultados

Se incluyen gráficos de:
- Predicción vs Realidad.
- Errores de los modelos.
- Comparativas de métricas.

También se ofrece una app construida con **Streamlit** para:
- Cargar nuevos datos.
- Probar los modelos entrenados.
- Visualizar métricas y predicciones.

---

## 🚀 App Streamlit

```bash
streamlit run app.py
```

Características:
- Interfaz limpia y profesional.
- Panel para selección de modelo.
- Visualizaciones de resultados.
- Predicción en tiempo real.

---

## 🗃️ Estructura del proyecto

```
.
├── DataCoSupplyChainDataset.csv
├── modelo_rf.pkl
├── modelo_xgb.pkl
├── streamlit_app/
│   └── app.py
├── notebooks/
│   └── model_training.ipynb
├── requirements.txt
└── README.md
```

---

## ⚙️ Requisitos

Instala dependencias con:

```bash
pip install -r requirements.txt
```

---

## 🙌 Autor

Proyecto realizado por Tomas Oviedo, como parte de estudiante de bootcamp de Data Science.
