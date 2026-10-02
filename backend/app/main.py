from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .pdf_service import generate_summary
from .ai_service import extract_text_from_pdf 
from .models import PDFAnalysisResponse


app = FastAPI(
    title="AI PDF Analyzer API",
    description="AI-powered PDF analysis and summarization API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
def health_check():
    return {
        "message": "AI PDF Analyzer API is running"
    }


@app.post(
    "/analyze-pdf",
    response_model=PDFAnalysisResponse,
    tags=["PDF Analyzer"],
    summary="Analyze PDF and generate Markdown summary",
)
async def analyze_pdf(
    file: UploadFile = File(
        ...,
        description="Upload a PDF document"
    )
):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    file_bytes = await file.read()

    try:

        text = extract_text_from_pdf(file_bytes)

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from PDF"
            )

        summary = generate_summary(text)

        return PDFAnalysisResponse(
            filename=file.filename,
            summary=summary
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )