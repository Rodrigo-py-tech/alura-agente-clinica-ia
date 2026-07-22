from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


# Cargar variables del archivo .env
load_dotenv()
print("GROQ:", os.getenv("GROQ_API_KEY"))

def crear_agente(vectorstore):

    # Crear buscador de documentos
    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 3
        }
    )


    # Obtener API KEY de Groq
    api_key = os.getenv("GROQ_API_KEY")


    if not api_key:
        raise ValueError(
            "No existe GROQ_API_KEY configurada. "
            "Verifica el archivo .env"
        )


    # Modelo LLM de Groq
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=api_key
    )


    # Prompt del agente RAG
    prompt = ChatPromptTemplate.from_template(
        """
        Eres Clínica Salud IA, un asistente virtual especializado
        en responder consultas relacionadas con información clínica.

        Utiliza únicamente el contexto proporcionado del documento.

        Si la información solicitada no se encuentra en el contexto,
        responde:
        "No tengo información suficiente en la documentación disponible."

        No inventes información.

        CONTEXTO:
        {context}


        PREGUNTA:
        {question}


        RESPUESTA:
        """
    )


    def responder(pregunta):

        # Buscar información relevante en la base vectorial
        documentos = retriever.invoke(
            pregunta
        )


        # Construir contexto
        if documentos:

            contexto = "\n\n".join(
                [
                    documento.page_content
                    for documento in documentos
                ]
            )

        else:

            contexto = (
                "No se encontró información relacionada "
                "en la documentación."
            )


        # Generar respuesta con IA
        respuesta = llm.invoke(
            prompt.format(
                context=contexto,
                question=pregunta
            )
        )


        return respuesta.content


    return responder