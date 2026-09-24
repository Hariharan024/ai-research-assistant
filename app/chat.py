from app.rag_pipeline import RAGPipeline


def start_chat():

    rag = RAGPipeline()

    print("\n================================")
    print("      AI RESEARCH ASSISTANT")
    print("================================")
    print("Ask questions about your document.")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if not question:
            continue

        answer, sources = rag.ask(question)

        print("\nAI:")
        print(answer)

        print("\nSources:")

        # Avoid displaying the same source/page multiple times
        displayed_sources = set()

        for source in sources:

            source_name = source["source"]
            page = source["page"]

            source_key = (source_name, page)

            if source_key not in displayed_sources:

                print(
                    f"  📄 {source_name} — Page {page}"
                )

                displayed_sources.add(source_key)

        print("\n" + "-" * 50)


if __name__ == "__main__":
    start_chat()