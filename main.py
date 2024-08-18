import streamlit as st
import pandas as pd
from datetime import date

# Inicialización del estado de la página
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Página 1"

# Función para cada página
def pagina1():


    # Inicializar la tabla si no existe en session_state
    if "gasto" not in st.session_state:
        st.session_state.gasto = pd.DataFrame(columns=["Descripción", "Categoría", "Monto", "Fecha"])

    # Formulario para ingresar gastos
    st.header("Registro de Gastos")
    with st.form("registro_form"):
        descripcion = st.text_input("Descripción del gasto")
        
        # Selección de categoría desde una lista
        categoria = st.selectbox("Categoría", ["Comida", "Transporte", "Entretenimiento", "Ropa", "Otros"])
        
        monto = st.number_input("Monto", min_value=0.0, format="%.2f")
        
        # Capturar la fecha de manera automática
        fecha = date.today()
        
        submitted = st.form_submit_button("Agregar Gasto")

        # Agregar nuevo registro a la tabla
        if submitted:
            nuevo_registro = pd.DataFrame({"Descripción": [descripcion], 
                                        "Categoría": [categoria], 
                                        "Monto": [monto], 
                                        "Fecha": [fecha]})
            st.session_state.gasto = pd.concat([st.session_state.gasto, nuevo_registro], ignore_index=True)

    # Mostrar la tabla con los registros acumulados
    st.write("Registros:")

    try:
        # Mostrar la tabla en un formato más compacto y ajustable, con desplazamiento horizontal
        st.dataframe(st.session_state.gasto, use_container_width=True)
    except Exception as e:
        st.error(f"Error al mostrar la tabla: {e}")


def pagina2():
    st.title("Dashboards de Gastos")
    
        # Botón para mostrar la gráfica de gastos por categoría
    if st.button("Mostrar gráfica de gastos por categoría"):
        if not st.session_state.gasto.empty:
            try:
                # Agrupar los gastos por categoría y sumar los montos
                gastos_por_categoria = st.session_state.gasto.groupby("Categoría")["Monto"].sum()

                # Mostrar la gráfica de barras con st.bar_chart
                st.bar_chart(gastos_por_categoria)
            except Exception as e:
                st.error(f"Error al generar la gráfica: {e}")
        else:
            st.write("No hay datos para mostrar en la gráfica.")
    
# Sidebar con botones para navegar entre páginas
st.sidebar.title("Navegación")
if st.sidebar.button("Registro de Gastos"):
    st.session_state.pagina = "Página 1"
if st.sidebar.button("Descripcion de Gastos"):
    st.session_state.pagina = "Página 2"
if st.sidebar.button("Insigths"):
    st.session_state.pagina = "Página 3"
    
    
# Mostrar la página seleccionada
if st.session_state.pagina == "Página 1":
    pagina1()
elif st.session_state.pagina == "Página 2":
    pagina2()