import streamlit as st
import tempfile

from src.ui import configurar_pagina
from src.ui import mostrar_sidebar

from src.pdf_loader import cargar_pdf
from src.pdf_loader import dividir_documentos

from src.vectorstore import crear_vectorstore
from src.agente import crear_agente


# Configuración inicial
configurar_pagina()


# Sidebar
archivo_pdf, limpiar = mostrar_sidebar()


# Inicializar variables de sesión
if "agente" not in st.session_state:
    st.session_state.agente = None


if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            "¡Hola! 👋 Soy tu asistente inteligente de Clínica Salud IA. "
            "Carga un PDF para comenzar a responder consultas."
        }
    ]


# ================================
# CARGA DEL PDF
# ================================

if archivo_pdf:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_pdf:

        temp_pdf.write(
            archivo_pdf.read()
        )

        ruta_pdf = temp_pdf.name


    documentos = cargar_pdf(
        ruta_pdf
    )


    chunks = dividir_documentos(
        documentos
    )


    vectorstore = crear_vectorstore(
        chunks
    )


    # Crear agente IA
    st.session_state.agente = crear_agente(
        vectorstore
    )


    st.success(
        "✅ Base vectorial creada correctamente"
    )


    st.info(
        f"Páginas cargadas: {len(documentos)}"
    )


    st.info(
        f"Fragmentos indexados: {len(chunks)}"
    )


# ================================
# INTERFAZ CHAT
# ================================

st.title(
    "🏥 Clínica Salud IA"
)


st.caption(
    "Challenge Final - Alura Agente Inteligente"
)


st.markdown("---")



# Mostrar historial

for mensaje in st.session_state.messages:

    with st.chat_message(
        mensaje["role"]
    ):

        st.markdown(
            mensaje["content"]
        )



# Entrada usuario

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

        st.markdown(
            pregunta
        )


    # ==========================
    # CONSULTA AL AGENTE
    # ==========================

    if st.session_state.agente:


        with st.chat_message("assistant"):


            with st.spinner(
                "Analizando documentos..."
            ):

                texto_respuesta = st.session_state.agente(
                        pregunta
                    )


                st.markdown(
                    texto_respuesta
                )


        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": texto_respuesta
            }
        )


    else:


        respuesta = (
            "⚠️ Primero debes cargar un documento PDF."
        )


        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": respuesta
            }
        )


        with st.chat_message("assistant"):

            st.markdown(
                respuesta
            )



# ================================
# LIMPIAR CHAT
# ================================

if limpiar:

    st.session_state.messages = []

    st.session_state.agente = None

    st.rerun()