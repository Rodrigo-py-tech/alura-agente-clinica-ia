from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


def crear_agente(vectorstore):


    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 3
        }
    )


    llm = ChatOllama(
        model="mistral",
        temperature=0
    )


    prompt = ChatPromptTemplate.from_template(
        """
        Eres un asistente inteligente de Clínica Salud IA.

        Responde utilizando solamente el contexto del documento.

        Si la respuesta no está en el contexto,
        indica que no tienes información suficiente.

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


        respuesta = llm.invoke(
            prompt.format(
                context=contexto,
                question=pregunta
            )
        )


        return respuesta.content


    return responder