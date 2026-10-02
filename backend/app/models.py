from pydantic import BaseModel


class PDFAnalysisResponse(BaseModel):
    filename: str
    summary: str