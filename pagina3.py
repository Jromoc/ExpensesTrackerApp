import streamlit as st

def mostrar_pagina():
    st.title("Chatbot")

    # Inicialización del estado para almacenar el historial de conversación
    if 'historial' not in st.session_state:
        st.session_state.historial = []

    # Título de la aplicación
    st.title("Chatbot en Streamlit (Interfaz Visual)")

    # Cuadro de texto para la pregunta del usuario
    pregunta = st.text_input("Escribe tu pregunta:")

    # Botón para enviar la pregunta
    if st.button("Enviar"):
        if pregunta:
            # Simula una respuesta del chatbot
            respuesta_simulada = "Esta es una respuesta simulada del chatbot."
            
            # Almacena la pregunta y la respuesta en el historial
            st.session_state.historial.append({"pregunta": pregunta, "respuesta": respuesta_simulada})

    # Mostrar el historial de conversación
    st.write("### Historial de conversación:")
    for i, intercambio in enumerate(st.session_state.historial, 1):
        st.write(f"**{i}.**")
        st.write(f"**Pregunta:** {intercambio['pregunta']}")
        st.write(f"**Respuesta:** {intercambio['respuesta']}")
    