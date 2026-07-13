from sentence_transformers import (
    SentenceTransformer
)

import chromadb


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="./vector_db"
)

collection = client.get_collection(
    "sap_knowledge"
)


def retrieve_context(
    query: str,
    top_k: int = 3
):

    embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return results["documents"][0]