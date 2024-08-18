import streamlit as st
import pandas as pd

# Inicializar la tabla si no existe en session_state
if "gasto" not in st.session_state:
    st.session_state.gasto = pd.DataFrame(columns=["Descripción", "Categoría", "Monto", "Fecha"])

 # Formulario para ingresar gastos
st.header("Registro de Gastos")
with st.form("registro_form"):
    descripcion = st.text_input("Descripción del gasto")
    categoria = st.selectbox("Categoría", ["Comida", "Transporte", "Entretenimiento", "Otros"])
    monto = st.number_input("Monto", min_value=0.0, format="%.2f")
    fecha = date.today()
    submitted = st.form_submit_button("Agregar Gasto")

    # Agregar nuevo registro a la tabla
    if submitted:
        nuevo_registro = pd.DataFrame({"Descrpcion": [descripcion], "Categoria": [categoria], "Monto": [monto], "Fecha": [fecha]})
        st.session_state.gasto = pd.concat([st.session_state.gasto, nuevo_registro], ignore_index=True)

# Mostrar la tabla con los registros acumulados
st.write("Registros:")
st.dataframe(st.session_state.gasto)
