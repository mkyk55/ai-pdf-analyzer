# AI PDF Analyzer

An AI-powered PDF analysis and document Q&A application built with **React, TypeScript, FastAPI, OpenAI, embeddings, and Retrieval-Augmented Generation (RAG)**.

The application allows users to upload a PDF, extract and process its content, generate an AI summary, and ask natural-language questions about the document.

---

## 🚀 Project Overview

AI PDF Analyzer converts unstructured PDF documents into searchable, understandable information.

The application currently supports:

* PDF upload
* PDF text extraction
* AI-generated Markdown summaries
* Document chunking
* Text embeddings
* In-memory vector storage
* Semantic similarity search
* RAG-based question answering
* Source chunk visibility
* React-based document chat interface
* FastAPI REST APIs
* Swagger/OpenAPI documentation

---

## 🏗️ Current Architecture

```text
                    React + TypeScript
                           │
             ┌─────────────┴─────────────┐
             │                           │
        Analyze PDF                  Chat with PDF
             │                           │
             ▼                           ▼
       POST /analyze-pdf             POST /ask
             │                           │
             ▼                           ▼
       PDF Text Extraction        Question Embedding
             │                           │
             ▼                           ▼
          Chunking                Vector Similarity
             │                           │
             ▼                           ▼
        Embeddings                  Top-K Chunks
             │                           │
             ▼                           ▼
       Vector Store ─────────────► OpenAI
                                         │
                                         ▼
                                  Grounded Answer
```

---

# ✨ Features

## 1. PDF Upload

Users can upload PDF documents through the React frontend.

The FastAPI backend validates the uploaded file and extracts its text using PyMuPDF.

---

## 2. AI PDF Summary

The `/analyze-pdf` endpoint:

```text
PDF
 ↓
Text Extraction
 ↓
OpenAI
 ↓
Markdown Summary
```

The generated summary contains:

* Executive Summary
* Key Points
* Important Facts
* Conclusion

---

## 3. Document Chunking

Large documents are divided into smaller overlapping chunks.

Current implementation:

```python
chunk_size = 1000
chunk_overlap = 200
```

Example:

```text
Document
   │
   ├── Chunk 1
   ├── Chunk 2
   ├── Chunk 3
   └── Chunk 4
```

Overlapping chunks help preserve context between neighboring sections.

---

## 4. Embeddings

Each document chunk is converted into a numerical vector representation.

```text
Text Chunk
    ↓
Embedding Model
    ↓
Vector
```

The embedding implementation is located at:

```text
backend/app/rag/embeddings.py
```

---

## 5. Vector Store

The project currently uses a simple in-memory vector store.

Location:

```text
backend/app/rag/vector_store.py
```

It stores:

```text
Text
Embedding
Metadata
```

and performs cosine similarity search.

```text
Query Vector
     ↓
Compare with stored vectors
     ↓
Calculate similarity
     ↓
Sort results
     ↓
Return Top-K
```

This implementation is intentionally simple so the underlying RAG concepts are easy to understand.

---

# 🤖 RAG Pipeline

The current Retrieval-Augmented Generation pipeline is:

```text
                 PDF
                  │
                  ▼
          Extract Text
                  │
                  ▼
              Chunking
                  │
                  ▼
             Embeddings
                  │
                  ▼
            Vector Store
                  │
                  │
          User Question
                  │
                  ▼
        Question Embedding
                  │
                  ▼
         Similarity Search
                  │
                  ▼
            Top-K Chunks
                  │
                  ▼
             OpenAI LLM
                  │
                  ▼
            Final Answer
```

The application instructs the generation model to answer using the retrieved document context rather than relying on unrelated external knowledge.

---

# 📁 Project Structure

```text
ai-pdf-analyzer/
│
├── backend/
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── pdf_service.py
│   │   ├── ai_service.py
│   │   ├── models.py
│   │   │
│   │   └── rag/
│   │       ├── __init__.py
│   │       ├── chunking.py
│   │       ├── embeddings.py
│   │       ├── vector_store.py
│   │       ├── rag_service.py
│   │       └── generation.py
│   │
│   ├── .env
│   ├── .gitignore
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.tsx
│   │   │   └── Loader.tsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── AnalyzePDF.tsx
│   │   │   └── ChatPDF.tsx
│   │   │
│   │   ├── App.tsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.tsx
│   │
│   ├── package.json
│   ├── vite.config.ts
│   └── index.html
│
├── .gitignore
└── README.md
```

---

# 🛠️ Technology Stack

## Frontend

* React
* TypeScript
* Vite
* React Router
* React Markdown
* CSS

## Backend

* Python
* FastAPI
* Pydantic
* Uvicorn
* PyMuPDF

## AI

* OpenAI API
* Embeddings
* LLM-based generation
* Retrieval-Augmented Generation

## Current Vector Search

* Custom Python in-memory vector store
* Cosine similarity

---

# 🔌 API Endpoints

## Health Check

```http
GET /
```

Example response:

```json
{
  "message": "AI PDF Analyzer API is running"
}
```

---

## Analyze PDF

```http
POST /analyze-pdf
```

Accepts:

```text
multipart/form-data
file = PDF
```

Processing:

```text
PDF
 ↓
Extract text
 ↓
Generate summary
 ↓
Chunk document
 ↓
Generate embeddings
 ↓
Store vectors
```

Example response:

```json
{
  "filename": "document.pdf",
  "summary": "# Executive Summary\n..."
}
```

---

## Ask Question

```http
POST /ask
```

Request:

```json
{
  "question": "What is the main purpose of this document?",
  "top_k": 3
}
```

Response:

```json
{
  "question": "What is the main purpose of this document?",
  "answer": "The document explains...",
  "sources": [
    {
      "filename": "document.pdf",
      "chunk_index": 0,
      "score": 0.82,
      "text": "..."
    }
  ]
}
```

---

# 🖥️ Frontend Routes

The React application currently provides:

| Route          | Purpose                              |
| -------------- | ------------------------------------ |
| `/`            | Home page                            |
| `/analyze-pdf` | Upload and analyze PDF               |
| `/chat`        | Ask questions about the uploaded PDF |

The dedicated Chat interface communicates with:

```text
POST /ask
```

---

# ⚙️ Installation

## Backend

Navigate to:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create:

```text
backend/.env
```

Add:

```env
OPENAI_API_KEY=your_api_key_here
```

Do not commit `.env` to GitHub.

---

## Start Backend

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# 🎨 Frontend Setup

Navigate to:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🧪 Testing the RAG Pipeline

The individual RAG components can be tested independently.

### Chunking

```python
from app.rag.chunking import split_text

chunks = split_text(document_text)

print(len(chunks))
```

### Embeddings

```python
from app.rag.embeddings import create_embedding

embedding = create_embedding(
    "Python is used for backend development."
)

print(type(embedding))
print(len(embedding))
```

### Vector Store

```python
from app.rag.vector_store import VectorStore

store = VectorStore()

store.add(
    texts=chunks,
    embeddings=embeddings
)

results = store.search(
    query_embedding=query_embedding,
    top_k=3
)
```

### RAG Service

```python
from app.rag.rag_service import RAGService

rag = RAGService()

rag.index_document(
    text=document_text,
    filename="document.pdf"
)

results = rag.retrieve(
    "What is the document about?",
    top_k=3
)
```

---

# 🔐 Security

The OpenAI API key is stored only on the backend.

```text
React
  │
  │ No API key
  ▼
FastAPI
  │
  │ API key
  ▼
OpenAI
```

The API key should never be placed in:

* React code
* TypeScript files
* `vite.config.ts`
* GitHub
* Browser local storage
* Public frontend environment variables

---

# ⚠️ Current Limitations

The current implementation is intentionally an educational/prototype architecture.

### In-memory vector store

All vectors disappear when the backend restarts.

```text
FastAPI restart
      ↓
Vector Store cleared
```

### Single active document

The current architecture clears the vector store when a new PDF is uploaded.

### No authentication

There is currently no user authentication or authorization.

### No persistent database

Documents, chunks, embeddings, and metadata are not persisted.

### Basic chunking

The current chunking strategy is character-based rather than semantic/token-aware.

### No page-level citations

The current metadata tracks chunk indexes but does not yet map retrieved chunks back to PDF page numbers.

---

# 🚧 Roadmap

## Phase 1 — Core RAG

* [x] PDF extraction
* [x] AI summarization
* [x] Chunking
* [x] Embeddings
* [x] Vector store
* [x] Cosine similarity
* [x] Semantic retrieval
* [x] RAG generation
* [x] `/ask` endpoint
* [x] React Chat with PDF page

## Phase 2 — Production RAG

* [ ] Document IDs
* [ ] Multiple document support
* [ ] Persistent vector database
* [ ] FAISS / Qdrant / pgvector
* [ ] Metadata filtering
* [ ] Page-level source references
* [ ] Better chunking
* [ ] Retrieval score threshold
* [ ] Conversation history

## Phase 3 — Full AI Application

* [ ] User authentication
* [ ] PostgreSQL
* [ ] Document storage
* [ ] User-specific documents
* [ ] Chat history
* [ ] Streaming responses
* [ ] Background document processing
* [ ] Rate limiting
* [ ] Error monitoring
* [ ] Production logging

## Phase 4 — Deployment

```text
React
   ↓
Azure / Static Hosting
   ↓
FastAPI
   ↓
Docker
   ↓
Azure App Service
   ↓
PostgreSQL
   ↓
Vector Database
   ↓
OpenAI
```

---

# 🎯 Future Architecture

The target production architecture is:

```text
                         User
                          │
                          ▼
                 React + TypeScript
                          │
                          ▼
                     FastAPI
                          │
                ┌─────────┴─────────┐
                │                   │
                ▼                   ▼
        Authentication          API Layer
                │                   │
                └─────────┬─────────┘
                          │
                          ▼
                     PostgreSQL
                          │
                          ▼
                  Document Storage
                          │
                          ▼
                  Document Processing
                          │
                          ▼
                      Chunking
                          │
                          ▼
                     Embeddings
                          │
                          ▼
               Vector Database
                 / Qdrant / pgvector
                          │
                          ▼
                    Retrieval
                          │
                          ▼
                       OpenAI
                          │
                          ▼
                  Grounded Response
                          │
                          ▼
                     React UI
```

---

# 💡 Possible Use Cases

The architecture can be extended for:

* Legal document analysis
* Contracts
* Technical documentation
* Research papers
* Financial reports
* HR policies
* Company documentation
* Compliance documents
* Government documents
* Internal knowledge bases

---

# 🧠 What This Project Demonstrates

This project demonstrates practical AI engineering concepts including:

* REST API development
* React + TypeScript
* Python backend engineering
* LLM integration
* Embeddings
* Vector search
* Semantic retrieval
* RAG architecture
* Prompt engineering
* Document processing
* API design
* Source-aware responses
* Full-stack AI application development

The goal is to evolve this project from a basic PDF summarizer into a **production-oriented document intelligence platform**.

---

# 👨‍💻 Author

**Mayank Kumar**

Python Developer | AI Engineering | Generative AI | RAG | FastAPI | React

---

## ⭐ Project Status

**Current status: Active Development**

The project is being developed incrementally to demonstrate the complete lifecycle of an AI-powered application:

```text
Prototype
   ↓
RAG
   ↓
Persistent Vector Database
   ↓
Authentication
   ↓
Production Architecture
   ↓
Docker
   ↓
Cloud Deployment
```
