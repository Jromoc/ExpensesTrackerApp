import streamlit as st

def mostrar_pagina():
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