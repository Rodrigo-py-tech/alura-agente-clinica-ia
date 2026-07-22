from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def crear_vectorstore(chunks):
    """
    Crea una base vectorial FAISS a partir de fragmentos
    ya procesados del documento.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )


    return vectorstore