# 🏥 Clínica Salud IA - Agente Inteligente RAG

## 📌 Descripción del Proyecto

Clínica Salud IA es un agente inteligente desarrollado como proyecto final del Challenge de Alura.

El objetivo principal es construir un asistente conversacional capaz de responder preguntas utilizando información contenida dentro de documentos PDF.

El sistema implementa una arquitectura RAG (Retrieval Augmented Generation), permitiendo que un modelo de lenguaje consulte una base de conocimiento propia antes de generar respuestas.

El usuario puede cargar un documento PDF y realizar preguntas relacionadas con su contenido.

# 🏗 Arquitectura de la Solución
                 Usuario
                   |
                   |
            Streamlit App
               app.py
                   |
    --------------------------------
                     |                              |

        Carga documento PDF Chat usuario
                    |
                    |
        pdf_loader.py
                    |
                    |
        División del documento
        RecursiveCharacterTextSplitter
                    |
                    |
        Generación de embeddings
        HuggingFace Embeddings
                    |
                    |
        Base Vectorial FAISS
                    |
                    |
        Recuperación semántica
        Retriever
                    |
                    |
        Modelo de lenguaje
        Ollama - Mistral
                    |
                    |
        Respuesta generada por IA

# 📂 Estructura del Proyecto
ALURA-AGENTE-CLINICA
    │
    ├── app.py
    │
    ├── src
    │ ├── agente.py
    │ ├── pdf_loader.py
    │ ├── vectorstore.py
    │ ├── ui.py
    │
    ├── documentos
    │ └── politica_privacidad.pdf
    │
    ├── screenshots
    │
    ├── requirements.txt
    │
    ├── README.md
    │
    └── .gitignore


# 🛠 Tecnologías utilizadas
## Lenguaje

- Python 3.x

## Framework Web

- Streamlit

Utilizado para crear la interfaz conversacional del agente.

## Inteligencia Artificial

- LangChain

Framework utilizado para construir el flujo RAG.


- Ollama

Modelo local utilizado:


Mistral


## Modelo de Embeddings

- HuggingFace Sentence Transformers

Modelo utilizado:

sentence-transformers/all-MiniLM-L6-v2


## Base Vectorial

- FAISS

Utilizado para almacenar y realizar búsquedas semánticas sobre los fragmentos del documento.


## Procesamiento de documentos

- PyPDFLoader

Permite extraer información desde archivos PDF.


- RecursiveCharacterTextSplitter

Divide documentos grandes en fragmentos optimizados para búsqueda.


# ⚙️ Instalación y ejecución
## 1. Clonar repositorio

```bash
git clone https://github.com/usuario/repositorio.git



💬 Ejemplos de preguntas al agente
Pregunta 1
¿Cuál es el objetivo principal del documento?

Respuesta esperada:

El objetivo principal del documento es establecer las políticas
y condiciones relacionadas con el uso del servicio.
Pregunta 2
¿Qué información protege la política de privacidad?

Respuesta esperada:

La política protege información personal proporcionada por los usuarios
y establece cómo será utilizada y almacenada.
Pregunta 3
¿Cuáles son las responsabilidades del usuario?

Respuesta esperada:

Según el documento, el usuario debe utilizar correctamente
los servicios y proporcionar información válida.


🚀 Características implementadas

✅ Carga dinámica de documentos PDF.

✅ Extracción automática de texto.

✅ División inteligente de documentos.

✅ Creación de embeddings.

✅ Base vectorial FAISS.

✅ Recuperación semántica.

✅ Integración con modelo LLM Mistral.

✅ Chat conversacional mediante Streamlit.

✅ Historial de conversación.

✅ Limpieza de sesión.



👨‍💻 Autor

Rodrigo Antonelli
Proyecto desarrollado como parte del Challenge Final - Alura Agente Inteligente.