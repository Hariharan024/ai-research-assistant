from app.vector_store import VectorStore
from tests.evaluation_questions import evaluation_questions


def evaluate_retrieval():

    store = VectorStore()

    total = len(evaluation_questions)
    correct = 0

    print("\n==============================")
    print("      RAG RETRIEVAL TEST")
    print("==============================")

    for item in evaluation_questions:

        question = item["question"]
        expected_pages = item["expected_pages"]

        results = store.search(
            question,
            top_k=3
        )

        metadatas = results["metadatas"][0]

        retrieved_pages = [
            metadata["page"]
            for metadata in metadatas
        ]

        found = any(
            page in expected_pages
            for page in retrieved_pages
        )

        if found:
            correct += 1

        print("\nQuestion:")
        print(question)

        print("Expected pages:")
        print(expected_pages)

        print("Retrieved pages:")
        print(retrieved_pages)

        print("Result:")
        print("PASS" if found else "FAIL")

    accuracy = correct / total

    print("\n==============================")
    print(f"Retrieval Accuracy: {accuracy:.2%}")
    print("==============================")


if __name__ == "__main__":
    evaluate_retrieval()