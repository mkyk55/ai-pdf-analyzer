# from typing import List, Dict, Any

# from .chunking import split_text
# from .embeddings import create_embedding, create_embeddings
# from .vector_store import VectorStore


# class RAGService:
#     """
#     Handles document indexing and semantic retrieval.
#     """

#     def __init__(self):
#         self.vector_store = VectorStore()

#     def index_document(
#         self,
#         text: str,
#         filename: str = "",
#     ) -> int:
#         """
#         Split a document into chunks, create embeddings,
#         and store them in the vector store.

#         Returns:
#             Number of chunks indexed.
#         """

#         # 1. Split document into chunks
#         chunks = split_text(text)

#         if not chunks:
#             return 0

#         # 2. Generate embeddings
#         embeddings = create_embeddings(chunks)

#         # 3. Create metadata
#         metadata = [
#             {
#                 "filename": filename,
#                 "chunk_index": index,
#             }
#             for index in range(len(chunks))
#         ]

#         # 4. Store chunks + embeddings
#         self.vector_store.add(
#             texts=chunks,
#             embeddings=embeddings,
#             metadata=metadata,
#         )

#         return len(chunks)

#     def retrieve(
#         self,
#         question: str,
#         top_k: int = 3,
#     ) -> List[Dict[str, Any]]:
#         """
#         Retrieve the most relevant chunks for a question.
#         """

#         if not question.strip():
#             raise ValueError("Question cannot be empty.")

#         # 1. Convert question into embedding
#         query_embedding = create_embedding(question)

#         # 2. Search vector store
#         results = self.vector_store.search(
#             query_embedding=query_embedding,
#             top_k=top_k,
#         )

#         return results

#     def clear(self) -> None:
#         """
#         Clear all indexed documents.
#         """

#         self.vector_store.clear()

#     def count(self) -> int:
#         """
#         Return number of indexed chunks.
#         """

#         return self.vector_store.count()

from typing import List, Dict, Any

from .chunking import split_text
from .embeddings import create_embedding, create_embeddings
from .vector_store import VectorStore


class RAGService:

    def __init__(self):
        self.vector_store = VectorStore()

    def index_document(
        self,
        text: str,
        filename: str = "",
    ) -> int:

        chunks = split_text(text)

        if not chunks:
            return 0

        embeddings = create_embeddings(chunks)

        metadata = [
            {
                "filename": filename,
                "chunk_index": index,
            }
            for index in range(len(chunks))
        ]

        self.vector_store.add(
            texts=chunks,
            embeddings=embeddings,
            metadata=metadata,
        )

        return len(chunks)

    def retrieve(
        self,
        question: str,
        top_k: int = 3,
    ) -> List[Dict[str, Any]]:

        if not question.strip():
            raise ValueError("Question cannot be empty.")

        query_embedding = create_embedding(question)

        return self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
        )

    def clear(self) -> None:
        self.vector_store.clear()

    def count(self) -> int:
        return self.vector_store.count()