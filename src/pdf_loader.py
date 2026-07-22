from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def cargar_pdf(ruta_pdf: str):
    """
    Carga un documento PDF y devuelve una lista de páginas.
    """
    loader = PyPDFLoader(ruta_pdf)
    documentos = loader.load()

    return documentos


def dividir_documentos(documentos):
    """
    Divide el documento en fragmentos para facilitar
    la búsqueda semántica.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.split_documents(documentos)

    return chunks