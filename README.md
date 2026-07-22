# 🏥 Clínica Salud IA - Agente Inteligente RAG

## 📌 Descripción General del Proyecto

**Clínica Salud IA** es un agente inteligente desarrollado como proyecto final del **Challenge Alura - Agentes de IA**.

El objetivo principal del proyecto es crear un asistente conversacional capaz de responder preguntas utilizando información contenida dentro de documentos PDF proporcionados por el usuario.

La solución implementa una arquitectura **RAG (Retrieval Augmented Generation)**, donde el modelo de lenguaje consulta una base de conocimiento propia antes de generar una respuesta, logrando respuestas más precisas y contextualizadas.

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
 Ollama - Mistral LLM
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
└── .gitignore                  # Archivos excluidos de Git
```

---

# 🛠 Tecnologías y Herramientas Utilizadas

## 🐍 Lenguaje de Programación

- **Python 3.x**

Lenguaje principal utilizado para desarrollar la aplicación y la integración con modelos de inteligencia artificial.

---

## 🌐 Framework Web

### Streamlit

Framework utilizado para construir la interfaz web interactiva del agente conversacional.

Permite:

- Carga de documentos.
- Interacción mediante chat.
- Visualización de respuestas.
- Gestión de la sesión del usuario.

---

## 🤖 Inteligencia Artificial

### LangChain

Framework utilizado para construir la arquitectura RAG, integrando:

- Carga de documentos.
- División de textos.
- Embeddings.
- Recuperación semántica.
- Comunicación con el modelo LLM.

---

### Ollama

Plataforma utilizada para ejecutar modelos de lenguaje localmente.

Modelo utilizado:

```
Mistral
```

---

## 🧠 Modelo de Embeddings

### HuggingFace Sentence Transformers

Modelo utilizado:

```
sentence-transformers/all-MiniLM-L6-v2
```

Responsable de convertir fragmentos de texto en vectores numéricos para realizar búsquedas semánticas.

---

## 🗄 Base Vectorial

### FAISS

Base vectorial utilizada para almacenar los embeddings generados y realizar búsquedas eficientes dentro del conocimiento del documento.

---

## 📄 Procesamiento de Documentos

### PyPDFLoader

Herramienta utilizada para:

- Lectura de documentos PDF.
- Extracción automática del contenido textual.

---

### RecursiveCharacterTextSplitter

Utilizado para dividir documentos grandes en fragmentos pequeños optimizados para la recuperación de información.

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

## 4. Ejecutar Ollama

Verificar que Ollama esté instalado y ejecutar el modelo:

```bash
ollama run mistral
```

---

## 5. Ejecutar aplicación Streamlit

```bash
streamlit run app.py
```

La aplicación estará disponible en:

```
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

> La política protege información personal proporcionada por los usuarios y establece cómo será utilizada y almacenada.

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

✅ Generación de embeddings.

✅ Base vectorial FAISS.

✅ Recuperación semántica mediante Retriever.

✅ Integración con modelo LLM Mistral.

✅ Arquitectura RAG completa.

✅ Chat conversacional mediante Streamlit.

✅ Historial de conversación.

✅ Limpieza de sesión.

---

# 📸 Capturas de Pantalla

Agregar aquí imágenes mostrando:

- Pantalla principal del agente.
- Carga del documento PDF.
- Ejemplo de conversación.
- Respuesta generada por IA.

Ejemplo:

```
screenshots/
│
├── inicio.png
├── carga_pdf.png
└── respuesta.png
```

---

# 📌 Conclusión

El proyecto demuestra la implementación de un agente inteligente basado en arquitectura **RAG**, combinando modelos de lenguaje, búsqueda semántica y procesamiento documental para crear un asistente capaz de responder consultas utilizando información personalizada.

---

# 👨‍💻 Autor

**Rodrigo Antonelli**

Proyecto desarrollado como parte del:

**Challenge Final - Alura Agentes Inteligentes**

Año: 2026