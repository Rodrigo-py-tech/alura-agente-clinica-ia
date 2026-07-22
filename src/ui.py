import streamlit as st


def configurar_pagina():

    st.set_page_config(
        page_title="Alura Agente Clínica IA",
        page_icon="🤖",
        layout="wide"
    )


def mostrar_sidebar():

    with st.sidebar:

        st.title("🤖 Alura Agente")

        st.markdown("---")

        st.write("### 📄 Documento")

        archivo = st.file_uploader(
            "Seleccione un documento PDF",
            type=["pdf"],
            help="Suba un documento para que el asistente pueda responder preguntas sobre su contenido."
        )

        st.markdown("---")

        limpiar = st.button("🗑 Limpiar conversación")

        return archivo, limpiar