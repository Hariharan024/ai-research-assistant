from app.vector_store import VectorStore


store = VectorStore()

results = store.search(
    "What is this document about?"
)

documents = results["documents"][0]

for i, document in enumerate(documents):

    print(f"\n--- Result {i + 1} ---")
    print(document)