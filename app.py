import streamlit as st
from pages import pagina1, pagina2, pagina3

# Sidebar para la navegación
st.sidebar.title("Navegación")
opcion = st.sidebar.radio("Ir a", ["Página 1", "Página 2", "Página 3"])

# Cargar la página seleccionada
if opcion == "Página 1":
    pagina1.mostrar_pagina()
elif opcion == "Página 2":
    pagina2.mostrar_pagina()
elif opcion == "Página 3":
    pagina3.mostrar_pagina()
