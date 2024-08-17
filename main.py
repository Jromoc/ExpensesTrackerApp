import streamlit as st
import pandas as pd

# Crear un DataFrame vacío
gastos = pd.DataFrame(columns=["Descripción", "Categoría", "Monto"])

# Formulario para ingresar gastos
st.header("Registro de Gastos")
descripcion = st.text_input("Descripción del gasto")
categoria = st.selectbox("Categoría", ["Comida", "Transporte", "Entretenimiento", "Otros"])
monto = st.number_input("Monto", min_value=0.0, format="%.2f")

if st.button("Agregar Gasto"):
    nuevo_gasto = pd.DataFrame({"Descripción": [descripcion], "Categoría": [categoria], "Monto": [monto]})
    gastos = pd.concat([gastos, nuevo_gasto], ignore_index=True)
    st.success("Gasto agregado!")

# Mostrar tabla de gastos
st.subheader("Tabla de Gastos")
st.dataframe(gastos)