from rag.retrieval import (
    retrieve_context
)

results = retrieve_context(
    "pricing transport risk"
)

print(
    "\n\n".join(results)
)