from typing import List, Dict, Any

from openai import OpenAI

from ..config import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)

GENERATION_MODEL = "gpt-5-mini"


def generate_answer(
    question: str,
    retrieved_chunks: List[Dict[str, Any]],
) -> str:

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    if not retrieved_chunks:
        return "I could not find relevant information in the document."

    context_parts = []

    for index, chunk in enumerate(
        retrieved_chunks,
        start=1
    ):
        context_parts.append(
            f"Context {index}:\n{chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are an AI document assistant.

Answer the user's question using ONLY the provided document context.

Rules:
- Do not use outside knowledge.
- If the answer is not present in the context, say:
  "The answer is not available in the provided document."
- Be concise and accurate.
- Explain the answer clearly.
- Do not mention the retrieval process.
- Do not invent information.

DOCUMENT CONTEXT:
----------------
{context}
----------------

USER QUESTION:
{question}

ANSWER:
"""

    response = client.responses.create(
        model=GENERATION_MODEL,
        input=prompt,
    )

    return response.output_text