# AI Research Assistant

A local LLM-powered Retrieval-Augmented Generation (RAG) system for asking questions about PDF documents.

The system allows users to upload PDF documents, process and index their content, and ask natural-language questions. Relevant document content is retrieved from a vector database and passed to a local Ollama language model to generate an answer with source information.

## Features

* Upload PDF documents through a web interface
* Extract text from PDF files
* Split documents into manageable chunks
* Generate embeddings for document chunks
* Store and retrieve document vectors using ChromaDB
* Rewrite user queries for improved retrieval
* Generate answers using a local Ollama LLM
* Return relevant sources with answers
* FastAPI backend
* React + Vite frontend
* Automated tests for core RAG components

## Architecture

```text
                    ┌─────────────────────┐
                    │   React + Vite UI   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI API      │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │    RAG Pipeline     │
                    └──────┬────────┬─────┘
                           │        │
                ┌──────────▼───┐    │
                │   ChromaDB   │    │
                │ Vector Store │    │
                └──────────────┘    │
                                    ▼
                           ┌────────────────┐
                           │ Ollama Local   │
                           │      LLM       │
                           └────────────────┘
```

## RAG Workflow

```text
PDF Upload
    ↓
PDF Text Extraction
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
ChromaDB Storage
    ↓
User Question
    ↓
Query Rewriting
    ↓
Relevant Chunk Retrieval
    ↓
Ollama Local LLM
    ↓
Answer + Sources
```

## Project Structure

```text
ai-research-assistant/
│
├── app/
│   ├── api.py
│   ├── chat.py
│   ├── chunker.py
│   ├── ingest.py
│   ├── local_llm.py
│   ├── pdf_loader.py
│   ├── query_rewriter.py
│   ├── rag_pipeline.py
│   ├── vector_store.py
│   └── __init__.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── index.html
│
├── tests/
│   ├── evaluation_questions.py
│   ├── test_chunker.py
│   ├── test_local_llm.py
│   ├── test_pdf_loader.py
│   ├── test_rag.py
│   ├── test_retrieval.py
│   └── test_vector_store.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Technologies Used

### Backend

* Python
* FastAPI
* Uvicorn

### RAG / AI

* Ollama
* ChromaDB
* Sentence Transformers
* Scikit-learn

### Document Processing

* PyPDF

### Frontend

* React
* Vite
* JavaScript

### Testing

* Pytest

## API Endpoints

### `GET /`

Checks whether the API is running.

### `POST /upload`

Uploads a PDF document and indexes its content.

The endpoint returns information including:

* Filename
* Number of extracted pages
* Number of generated chunks

### `POST /ask`

Accepts a natural-language question and optionally a source document.

Returns:

* Generated answer
* Relevant sources

## Local Setup

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd ai-research-assistant
```

### 2. Create a Python virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Python dependencies

```powershell
pip install -r requirements.txt
```

### 4. Install and run Ollama

Install Ollama and make sure the required local model is available.

Verify Ollama is running:

```powershell
ollama list
```

If your project uses a specific model, make sure that model is installed before starting the application.

### 5. Start the FastAPI backend

From the project root:

```powershell
uvicorn app.api:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 6. Start the frontend

Open another terminal:

```powershell
cd frontend
npm install
npm run dev
```

The Vite development server will normally be available at:

```text
http://localhost:5173
```

## Testing

From the project root:

```powershell
pytest
```

Individual test files can also be executed separately.

## Important Notes

This project uses a **local LLM through Ollama** rather than requiring an OpenAI API key.

The following local/generated files are intentionally excluded from the repository:

```text
.venv/
data/
node_modules/
__pycache__/
```

Users can provide their own PDF documents locally for testing and indexing.

## Project Goal

The goal of this project is to explore how Retrieval-Augmented Generation can be used to build a document-focused research assistant that provides answers based on user-provided documents rather than relying only on the model's general knowledge.

## Status

 actively being developed and improved.
