# 🤖 AI PDF Analyzer

An AI-powered document intelligence application that allows users to upload PDF documents and automatically generate structured, easy-to-understand summaries using **FastAPI, React, TypeScript, PyMuPDF, and OpenAI**.

The project demonstrates an end-to-end AI application workflow — from document upload and text extraction to LLM-powered analysis and Markdown rendering.

---

## 🚀 Features

* 📄 Upload PDF documents
* 🔍 Extract text from PDFs using PyMuPDF
* 🤖 Analyze document content using OpenAI
* 📝 Generate structured Markdown summaries
* 📌 Extract key points and important facts
* 💡 Generate an executive summary and conclusion
* ⚡ Real-time analysis status and loading indicator
* 🎨 Responsive React + TypeScript interface
* 🔗 REST API built with FastAPI
* 📚 Interactive Swagger API documentation
* 🔐 API key kept securely on the backend

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   React + TypeScript │
                    │      Frontend       │
                    └──────────┬──────────┘
                               │
                         PDF Upload
                               │
                               ▼
                    ┌─────────────────────┐
                    │       FastAPI       │
                    │       Backend       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      PyMuPDF        │
                    │   Text Extraction   │
                    └──────────┬──────────┘
                               │
                         Document Text
                               │
                               ▼
                    ┌─────────────────────┐
                    │      OpenAI API     │
                    │    AI Analysis      │
                    └──────────┬──────────┘
                               │
                       Markdown Summary
                               │
                               ▼
                    ┌─────────────────────┐
                    │   React Markdown    │
                    │    Result Viewer    │
                    └─────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend

* React
* TypeScript
* Vite
* React Router
* React Markdown
* CSS

### Backend

* Python
* FastAPI
* Uvicorn
* PyMuPDF
* Pydantic
* Python-dotenv

### AI

* OpenAI API
* LLM-based document analysis
* Structured Markdown generation

---

## 📁 Project Structure

```text
ai-pdf-analyzer/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── pdf_service.py
│   │   ├── ai_service.py
│   │   └── models.py
│   │
│   ├── .env
│   ├── .gitignore
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.tsx
│   │   │   └── Loader.tsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   └── AnalyzePDF.tsx
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

# ⚙️ Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/mkyk55/ai-pdf-analyzer.git

cd ai-pdf-analyzer
```

---

# 🐍 Backend Setup

Navigate to the backend:

```bash
cd backend
```

## Create a Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create:

```text
backend/.env
```

Add:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

⚠️ **Never commit your real API key to GitHub.**

The `.env` file should remain in `.gitignore`.

---

## Start the Backend

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# ⚛️ Frontend Setup

Open another terminal.

Navigate to:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

# 📄 How to Use

1. Open the application.
2. Navigate to **Analyze PDF**.
3. Select a PDF document.
4. Click **Analyze PDF**.
5. The frontend sends the document to the FastAPI backend.
6. PyMuPDF extracts the document text.
7. The extracted text is sent to the OpenAI API.
8. The AI generates a structured Markdown summary.
9. The frontend renders the Markdown result.

The generated analysis contains:

```text
Executive Summary
        ↓
Key Points
        ↓
Important Facts
        ↓
Conclusion
```

---

# 🔌 API

## Analyze PDF

### Endpoint

```http
POST /analyze-pdf
```

### Request

Multipart form-data:

```text
file: <PDF document>
```

### Example Response

```json
{
  "filename": "example.pdf",
  "summary": "# Executive Summary\n\nThis document..."
}
```

---

# 🧠 AI Processing

The current AI pipeline uses the following flow:

```text
PDF
 ↓
Text Extraction
 ↓
Document Text
 ↓
Prompt Construction
 ↓
OpenAI API
 ↓
AI Generated Analysis
 ↓
Markdown
 ↓
React Markdown Renderer
```

The AI is instructed to produce a consistent structure containing:

* Executive Summary
* Key Points
* Important Facts
* Conclusion

---

# 🔐 Security

The OpenAI API key is stored only on the backend.

```text
React Frontend
      │
      │ PDF
      ▼
FastAPI Backend
      │
      │ API Key
      ▼
OpenAI API
```

The frontend never receives or exposes the OpenAI API key.

For production deployments, environment variables or a secure secret-management solution should be used.

---

# 🚧 Current Limitations

The current version focuses on text-based PDF documents.

Potential limitations include:

* Scanned/image-only PDFs require OCR.
* Very large documents may exceed model context limits.
* The current version processes the complete extracted document rather than using retrieval.
* No persistent document storage yet.
* No user authentication yet.

---

# 🛣️ Roadmap

The project is being developed toward a more complete **AI Document Intelligence Platform**.

### Phase 1 — Core Application

* [x] React frontend
* [x] TypeScript
* [x] FastAPI backend
* [x] PDF upload
* [x] PDF text extraction
* [x] OpenAI integration
* [x] Markdown summaries
* [x] Swagger API documentation

### Phase 2 — Advanced AI

* [ ] Document chunking
* [ ] Embeddings
* [ ] Vector database
* [ ] RAG pipeline
* [ ] Ask questions about documents
* [ ] Source/page citations
* [ ] Multi-document analysis
* [ ] Conversation history

### Phase 3 — Production Engineering

* [ ] Authentication
* [ ] PostgreSQL
* [ ] Document storage
* [ ] Background processing
* [ ] Rate limiting
* [ ] Logging and monitoring
* [ ] Docker
* [ ] CI/CD
* [ ] Azure deployment

### Phase 4 — Advanced Document Intelligence

* [ ] OCR support
* [ ] Table extraction
* [ ] Document classification
* [ ] Semantic search
* [ ] Document comparison
* [ ] AI-generated questions
* [ ] Structured data extraction
* [ ] Agentic document workflows

---

# 🎯 Project Goals

This project is designed to demonstrate practical skills in:

* Full-stack AI application development
* LLM integration
* REST API development
* Document processing
* Prompt engineering
* AI application architecture
* React + TypeScript
* Python backend development
* RAG architecture
* Cloud deployment
* Production-oriented AI engineering

---

# 📈 Future Architecture

The long-term architecture will evolve toward:

```text
                    React + TypeScript
                           │
                           ▼
                      FastAPI API
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
              Authentication   PostgreSQL
                                  │
                                  ▼
                         Document Storage
                                  │
                                  ▼
                         Text Extraction
                                  │
                                  ▼
                           Chunking
                                  │
                                  ▼
                          Embeddings
                                  │
                                  ▼
                         Vector Database
                                  │
                                  ▼
                              RAG
                                  │
                                  ▼
                            OpenAI LLM
                                  │
                                  ▼
                       Structured Response
                                  │
                                  ▼
                         React Application
```

---

# 👨‍💻 Author

**Mayank Kumar**

GitHub: **[@mkyk55](https://github.com/mkyk55)**

---

## ⭐ Contributing

Contributions, suggestions, and improvements are welcome.

If you find the project useful, consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is intended for learning, experimentation, and portfolio development.
