import streamlit as st
import pandas as pd
from datetime import date

# Inicializar la tabla si no existe en session_state
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Descripción", "Categoría", "Monto", "Fecha"])

# Formulario para agregar un nuevo registro
with st.form("registro_form"):
    descripcion = st.text_input("Descripción del gasto")
    categoria = st.text_input("Categoría")
    monto = st.number_input("Monto", min_value=0.0)
    
    # Puedes usar st.date_input para que el usuario elija la fecha manualmente
    # fecha = st.date_input("Fecha", value=date.today())
    
    # O capturar automáticamente la fecha de hoy cuando se agrega el registro
    fecha = date.today()
    
    submitted = st.form_submit_button("Agregar Registro")

    # Agregar nuevo registro a la tabla
    if submitted:
        nuevo_registro = pd.DataFrame({"Descripción": [descripcion], 
                                       "Categoría": [categoria], 
                                       "Monto": [monto], 
                                       "Fecha": [fecha]})
        st.session_state.data = pd.concat([st.session_state.data, nuevo_registro], ignore_index=True)

# Mostrar la tabla con los registros acumulados
st.write("Registros:")
st.dataframe(st.session_state.data)
