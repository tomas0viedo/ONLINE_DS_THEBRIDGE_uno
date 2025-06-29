import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="📈 Predicción de Demanda - Demo", layout="wide")
st.title("🔮 Sistema de Predicción de Demanda")

# Carga modelos y scaler
model_rf = joblib.load('model_rf.pkl')
model_xgb = joblib.load('model_xgb.pkl')
model_lgb = joblib.load('model_lgb.pkl')
scaler = joblib.load('scaler.pkl')

# Variables numéricas para escalar (igual que en entrenamiento)
num_cols = ['Sales', 'Order Profit Per Order', 'Year', 'Month', 'Day_of_Week']

# Columnas que espera el modelo (igual que X_train)
model_columns = joblib.load('model_columns.pkl')  # Guarda previamente las columnas usadas en el entrenamiento

# Lista de departamentos
departamentos = [
    'Apparel', 'Book Shop', 'Discs Shop', 'Fan Shop', 'Fitness', 'Footwear',
    'Golf', 'Health and Beauty ', 'Outdoors', 'Pet Shop', 'Technology'
]

st.info("""
⚠️ **Nota:** Datos históricos de 2015-2018.  
Las predicciones son aproximadas y orientativas para practicar.
""")

with st.form("form_pred"):
    fecha_input = st.date_input("Fecha del pedido")
    departamento_input = st.selectbox("Departamento", departamentos)
    ventas_input = st.number_input("Ventas ($)", min_value=0.0, step=10.0)
    ganancia_input = st.number_input("Ganancia por orden ($)", min_value=0.0, step=1.0)
    modelo_elegido = st.selectbox("Selecciona modelo para predecir", ["Random Forest", "XGBoost", "LightGBM"])
    submit = st.form_submit_button("Predecir")

if submit:
    year = fecha_input.year
    month = fecha_input.month
    day_of_week = fecha_input.weekday()

    # Crear diccionario de input
    input_data = {
        'Sales': ventas_input,
        'Order Profit Per Order': ganancia_input,
        'Year': year,
        'Month': month,
        'Day_of_Week': day_of_week
    }

    # Añadir variables one-hot para departamentos
    for dept in departamentos:
        col_name = f"Department Name_{dept}"
        input_data[col_name] = 1 if dept == departamento_input else 0

    # Crear dataframe con todas las columnas necesarias
    input_df = pd.DataFrame(columns=model_columns)
    input_df.loc[0] = 0  # inicializa en 0
    for col in input_data:
        if col in input_df.columns:
            input_df.at[0, col] = input_data[col]

    # Escalar numéricas
    input_df[num_cols] = scaler.transform(input_df[num_cols])

    # Elegir modelo
    modelos = {
        "Random Forest": model_rf,
        "XGBoost": model_xgb,
        "LightGBM": model_lgb
    }
    modelo = modelos[modelo_elegido]

    # Predecir
    prediccion = modelo.predict(input_df)[0]

    st.success(f"✅ Predicción estimada: **{prediccion:.2f} unidades** usando **{modelo_elegido}** (simulador).")