import streamlit as st
from . import pagina3
from . import pagina1, pagina2



# Sidebar con botones para navegar entre páginas
st.sidebar.title("Navegación")
if st.sidebar.button("Registro de Gastos"):
    pagina1.mostrar_pagina()
if st.sidebar.button("Descripcion de Gastos"):
    pagina2.mostrar_pagina()
if st.sidebar.button("Chatbot"):
    pagina3.mostrar_pagina()
    
    
