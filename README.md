# 🏥 Clínica Salud IA - Agente Inteligente RAG

## 📌 Descripción General del Proyecto

**Clínica Salud IA** es un agente inteligente desarrollado como proyecto final del **Challenge Alura - Agentes de IA**.

El objetivo principal del proyecto es crear un asistente conversacional capaz de responder preguntas utilizando información contenida en documentos PDF proporcionados por el usuario.

La solución implementa una arquitectura **RAG (Retrieval-Augmented Generation)**, donde un modelo de lenguaje consulta una base de conocimiento construida a partir del contenido del documento antes de generar una respuesta, ofreciendo respuestas más precisas, contextualizadas y alineadas con la información disponible.

La aplicación utiliza **Groq** como proveedor del modelo de lenguaje (LLM), **LangChain** para la orquestación del flujo RAG, **FAISS** como base vectorial y **Hugging Face Embeddings** para la representación semántica del contenido.

El usuario puede cargar documentos PDF, realizar consultas sobre su contenido y obtener respuestas generadas mediante inteligencia artificial.

---

# 🏗 Arquitectura de la Solución

La aplicación implementa el siguiente flujo:

```text
                 Usuario
                    |
                    |
             Streamlit App
                app.py
                    |
                    |
        -----------------------------
        |                           |
 Carga documento PDF          Chat usuario
        |
        |
     pdf_loader.py
        |
        |
 Extracción de texto PDF
        |
        |
 RecursiveCharacterTextSplitter
 División del documento en fragmentos
        |
        |
 HuggingFace Embeddings
 Generación de vectores
        |
        |
       FAISS
 Base vectorial de conocimiento
        |
        |
     Retriever
 Recuperación semántica
        |
        |
  Groq (Llama 3.1 8B Instant)
 Generación de respuesta
        |
        |
 Respuesta final al usuario
```

---

# 📂 Estructura del Proyecto

```text
ALURA-AGENTE-CLINICA
│
├── app.py                      # Aplicación principal Streamlit
│
├── src
│   ├── agente.py               # Lógica del agente RAG
│   ├── pdf_loader.py           # Carga y procesamiento de PDFs
│   ├── vectorstore.py          # Creación de base vectorial FAISS
│   └── ui.py                   # Componentes de interfaz
│
├── documentos
│   └── politica_privacidad.pdf # Documento utilizado como fuente
│
├── screenshots                 # Capturas de pantalla del proyecto
│
├── requirements.txt            # Dependencias del proyecto
│
├── README.md                   # Documentación
│
├── .gitignore                  # Archivos excluidos de Git
│
└── .env.example                # Variables de entorno de ejemplo
```

---

# 🛠 Tecnologías y Herramientas Utilizadas

## 🐍 Lenguaje de Programación

* **Python 3.x**

Lenguaje principal utilizado para desarrollar la aplicación y la integración con modelos de inteligencia artificial.

---

## 🌐 Framework Web

### Streamlit

Framework utilizado para construir la interfaz web interactiva del agente conversacional.

Permite:

* Carga de documentos PDF.
* Interacción mediante chat.
* Visualización de respuestas.
* Gestión de la sesión del usuario.

---

## 🤖 Inteligencia Artificial

### LangChain

Framework utilizado para implementar la arquitectura RAG, integrando:

* Carga de documentos.
* División de textos.
* Embeddings.
* Recuperación semántica.
* Comunicación con el modelo de lenguaje.

---

### Groq

Proveedor de inferencia de modelos de lenguaje de alta velocidad mediante API.

Modelo utilizado:

```text
llama-3.1-8b-instant
```

Groq permite generar respuestas rápidas y eficientes a partir del contexto recuperado por la arquitectura RAG.

---

## 🧠 Modelo de Embeddings

### Hugging Face Sentence Transformers

Modelo utilizado:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Responsable de convertir los fragmentos de texto en vectores numéricos para realizar búsquedas semánticas.

---

## 🗄 Base Vectorial

### FAISS

Base vectorial utilizada para almacenar los embeddings generados y realizar búsquedas eficientes dentro del conocimiento del documento.

---

## 📄 Procesamiento de Documentos

### PyPDFLoader

Herramienta utilizada para:

* Lectura de documentos PDF.
* Extracción automática del contenido textual.

---

### RecursiveCharacterTextSplitter

Utilizado para dividir documentos grandes en fragmentos optimizados para la recuperación de información.

---

# ⚙️ Instalación y Ejecución

## 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/alura-agente-clinica.git
```

Ingresar al proyecto:

```bash
cd alura-agente-clinica
```

---

## 2. Crear entorno virtual

```bash
python -m venv .venv
```

Activar entorno virtual:

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Configurar la API Key de Groq

Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
GROQ_API_KEY=tu_api_key_de_groq
```

La API Key puede obtenerse desde la consola de Groq.

---

## 5. Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación estará disponible en:

```text
http://localhost:8501
```

---

# 💬 Ejemplos de Preguntas que el Agente Puede Responder

## Pregunta 1

**¿Cuál es el objetivo principal del documento?**

Respuesta generada:

> El objetivo principal del documento es establecer las políticas y condiciones relacionadas con el uso del servicio.

---

## Pregunta 2

**¿Qué información protege la política de privacidad?**

Respuesta generada:

> La política protege la información personal proporcionada por los usuarios y establece cómo será utilizada y almacenada.

---

## Pregunta 3

**¿Cuáles son las responsabilidades del usuario?**

Respuesta generada:

> Según el documento, el usuario debe utilizar correctamente los servicios y proporcionar información válida.

---

# 🚀 Características Implementadas

✅ Carga dinámica de documentos PDF.

✅ Extracción automática de información.

✅ División inteligente de documentos.

✅ Generación de embeddings con Hugging Face.

✅ Base vectorial FAISS.

✅ Recuperación semántica mediante Retriever.

✅ Integración con Groq (Llama 3.1 8B Instant).

✅ Arquitectura RAG completa.

✅ Chat conversacional mediante Streamlit.

✅ Historial de conversación.

✅ Limpieza de sesión.

---

# 📸 Capturas de Pantalla

Agregar imágenes mostrando:

* Pantalla principal del agente.
* Carga del documento PDF.
* Ejemplo de conversación.
* Respuesta generada por IA.

Ejemplo:

```text
screenshots/
│
├── inicio.png
├── carga_pdf.png
└── respuesta.png
```

---

# 📌 Conclusión

El proyecto demuestra la implementación de un agente inteligente basado en arquitectura **Retrieval-Augmented Generation (RAG)**, combinando procesamiento documental, búsqueda semántica y modelos de lenguaje para ofrecer respuestas precisas fundamentadas en el contenido de documentos PDF.

La integración de **Groq**, **LangChain**, **FAISS** y **Hugging Face Embeddings** permite construir una solución moderna, escalable y eficiente para consultas inteligentes sobre documentación personalizada.

---

# 👨‍💻 Autor

**Rodrigo Antonelli**

Proyecto desarrollado como parte del:

**Challenge Final - Alura Agentes Inteligentes**

Año: **2026**
