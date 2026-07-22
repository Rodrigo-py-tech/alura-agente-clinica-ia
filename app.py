import streamlit as st

from src.ui import configurar_pagina
from src.ui import mostrar_sidebar


configurar_pagina()

archivo_pdf, limpiar = mostrar_sidebar()


st.title("🏥 Clínica Salud IA")

st.caption(
    "Challenge Final - Alura Agente"
)

st.markdown("---")


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "¡Hola! 👋 Soy tu asistente inteligente. En la siguiente fase podré responder preguntas sobre un documento PDF."
        }
    ]


for mensaje in st.session_state.messages:

    with st.chat_message(mensaje["role"]):

        st.markdown(mensaje["content"])


pregunta = st.chat_input(
    "Escriba su pregunta..."
)


if pregunta:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": pregunta
        }
    )

    with st.chat_message("user"):
        st.markdown(pregunta)

    respuesta = (
        "Todavía no tengo un documento cargado. "
        "En la próxima fase aprenderé a leer PDFs."
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": respuesta
        }
    )

    with st.chat_message("assistant"):
        st.markdown(respuesta)


if limpiar:

    st.session_state.messages = []

    st.rerun()