from typing import List


def split_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> List[str]:
    """
    Split document text into overlapping chunks.

    Args:
        text: Complete document text.
        chunk_size: Maximum number of characters per chunk.
        chunk_overlap: Number of characters shared between chunks.

    Returns:
        A list of text chunks.
    """

    if not text.strip():
        return []

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size"
        )

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - chunk_overlap
    print(f"Total chunks created: {len(chunks)}")    

    return chunks