from sentence_transformers import (
    SentenceTransformer
)

import chromadb
import os


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient( # Without PersistentClient, everything would disappear when the program exits
    path="./vector_db"
)

collection = client.get_or_create_collection(
    "sap_knowledge"
)


for filename in os.listdir(
    "knowledge_base"
):

    with open(
        f"knowledge_base/{filename}",
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    embedding = model.encode(
        content
    ).tolist()

    collection.add(
        ids=[filename],
        documents=[content],
        embeddings=[embedding]
    )

print(
    "Knowledge base indexed."
)