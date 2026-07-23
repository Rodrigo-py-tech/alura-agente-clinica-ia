from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


load_dotenv()


def crear_agente(vectorstore):

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 3
        }
    )


    api_key = os.getenv("GROQ_API_KEY")


    if not api_key:
        raise ValueError(
            "No existe GROQ_API_KEY configurada"
        )


    # Modelo Groq
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=api_key
    )


    prompt = ChatPromptTemplate.from_template(
        """
        Eres Consultas IA, un asistente virtual.

        Responde utilizando solamente el contexto entregado.

        Si la información no aparece en el contexto,
        indica que no existe información suficiente.

        CONTEXTO:
        {context}

        PREGUNTA:
        {question}

        RESPUESTA:
        """
    )


    def responder(pregunta):

        documentos = retriever.invoke(
            pregunta
        )


        contexto = "\n\n".join(
            [
                doc.page_content
                for doc in documentos
            ]
        )


        mensaje = prompt.format(
            context=contexto,
            question=pregunta
        )


        respuesta = llm.invoke(
            mensaje
        )


        return respuesta.content


    return responder