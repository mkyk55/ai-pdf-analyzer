from typing import List

from openai import OpenAI

from ..config import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)


EMBEDDING_MODEL = "text-embedding-3-small"


def create_embedding(text: str) -> List[float]:
    """
    Convert a single text chunk into an embedding vector.
    """

    if not text.strip():
        raise ValueError("Text cannot be empty.")

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )

    return response.data[0].embedding


def create_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Convert multiple text chunks into embedding vectors.
    """

    if not texts:
        return []

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts,
    )

    return [
        item.embedding
        for item in response.data
    ]