from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException,
)

from fastapi.middleware.cors import CORSMiddleware

from .pdf_service import generate_summary
from .ai_service import extract_text_from_pdf
from .models import (
    PDFAnalysisResponse,
    AskRequest,
    AskResponse,
)

from .rag.rag_service import RAGService
from .rag.generation import generate_answer


app = FastAPI(
    title="AI PDF Analyzer API",
    description="AI-powered PDF analysis and RAG API",
    version="2.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------
# RAG Service
# ---------------------------------------

rag_service = RAGService()


# ---------------------------------------
# Health Check
# ---------------------------------------

@app.get(
    "/",
    tags=["Health"]
)
def health_check():

    return {
        "message": "AI PDF Analyzer API is running"
    }


# ---------------------------------------
# PDF Analysis
# ---------------------------------------

@app.post(
    "/analyze-pdf",
    response_model=PDFAnalysisResponse,
    tags=["PDF Analyzer"],
)
async def analyze_pdf(
    file: UploadFile = File(...)
):

    if file.content_type != "application/pdf":

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed",
        )

    file_bytes = await file.read()

    try:

        text = extract_text_from_pdf(
            file_bytes
        )

        if not text.strip():

            raise HTTPException(
                status_code=400,
                detail="Could not extract text from PDF",
            )

        # Existing summarization
        summary = generate_summary(text)

        # New RAG indexing
        rag_service.clear()

        chunks_indexed = rag_service.index_document(
            text=text,
            filename=file.filename or "",
        )

        return PDFAnalysisResponse(
            filename=file.filename or "",
            summary=summary,
        )

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ---------------------------------------
# Ask Question
# ---------------------------------------

@app.post(
    "/ask",
    response_model=AskResponse,
    tags=["RAG"],
)
async def ask_question(
    request: AskRequest,
):

    if not request.question.strip():

        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty",
        )

    try:

        # Retrieve relevant chunks
        results = rag_service.retrieve(
            question=request.question,
            top_k=request.top_k,
        )

        if not results:

            return AskResponse(
                question=request.question,
                answer=(
                    "No relevant information was found "
                    "in the uploaded document."
                ),
                sources=[],
            )

        # Generate answer using retrieved context
        answer = generate_answer(
            question=request.question,
            retrieved_chunks=results,
        )

        # Return source information
        sources = [
            {
                "filename": result["metadata"].get(
                    "filename"
                ),
                "chunk_index": result["metadata"].get(
                    "chunk_index"
                ),
                "score": result["score"],
                "text": result["text"],
            }
            for result in results
        ]

        return AskResponse(
            question=request.question,
            answer=answer,
            sources=sources,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )