from typing import List, Dict, Any
import math


class VectorStore:
    """
    Simple in-memory vector store.

    Stores:
        - text chunks
        - embeddings
        - optional metadata

    Provides:
        - add documents
        - similarity search
    """

    def __init__(self):
        self.documents: List[Dict[str, Any]] = []

    def add(
        self,
        texts: List[str],
        embeddings: List[List[float]],
        metadata: List[Dict[str, Any]] | None = None,
    ) -> None:
        """
        Add text chunks and their embeddings to the vector store.
        """

        if len(texts) != len(embeddings):
            raise ValueError(
                "Number of texts must match number of embeddings."
            )

        if metadata is not None and len(metadata) != len(texts):
            raise ValueError(
                "Number of metadata items must match number of texts."
            )

        for index, (text, embedding) in enumerate(
            zip(texts, embeddings)
        ):
            self.documents.append(
                {
                    "text": text,
                    "embedding": embedding,
                    "metadata": (
                        metadata[index]
                        if metadata
                        else {}
                    ),
                }
            )

    @staticmethod
    def cosine_similarity(
        vector_a: List[float],
        vector_b: List[float],
    ) -> float:
        """
        Calculate cosine similarity between two vectors.
        """

        if len(vector_a) != len(vector_b):
            raise ValueError(
                "Vectors must have the same dimensions."
            )

        dot_product = sum(
            a * b
            for a, b in zip(vector_a, vector_b)
        )

        magnitude_a = math.sqrt(
            sum(a * a for a in vector_a)
        )

        magnitude_b = math.sqrt(
            sum(b * b for b in vector_b)
        )

        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0

        return dot_product / (
            magnitude_a * magnitude_b
        )

    def search(
        self,
        query_embedding: List[float],
        top_k: int = 3,
    ) -> List[Dict[str, Any]]:
        """
        Find the most semantically similar documents.
        """

        if not self.documents:
            return []

        results = []

        for document in self.documents:

            score = self.cosine_similarity(
                query_embedding,
                document["embedding"],
            )

            results.append(
                {
                    "text": document["text"],
                    "metadata": document["metadata"],
                    "score": score,
                }
            )

        results.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return results[:top_k]

    def count(self) -> int:
        """
        Return number of stored documents.
        """

        return len(self.documents)

    def clear(self) -> None:
        """
        Remove all stored documents.
        """

        self.documents.clear()