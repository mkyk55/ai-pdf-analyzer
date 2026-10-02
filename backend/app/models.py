from pydantic import BaseModel


class PDFAnalysisResponse(BaseModel):
    filename: str
    summary: str


class AskRequest(BaseModel):
    question: str
    top_k: int = 3


class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[dict]