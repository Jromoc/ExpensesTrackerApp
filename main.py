import streamlit as st
import pandas as pd

# Inicializar la tabla si no existe en session_state
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Nombre", "Edad", "Ciudad"])

# Formulario para agregar un nuevo registro
with st.form("registro_form"):
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", min_value=0)
    ciudad = st.text_input("Ciudad")
    submitted = st.form_submit_button("Agregar Registro")

    # Agregar nuevo registro a la tabla
    if submitted:
        nuevo_registro = pd.DataFrame({"Nombre": [nombre], "Edad": [edad], "Ciudad": [ciudad]})
        st.session_state.data = pd.concat([st.session_state.data, nuevo_registro], ignore_index=True)

# Mostrar la tabla con los registros acumulados
st.write("Registros:")
st.dataframe(st.session_state.data)
