from app.rag_pipeline import RAGPipeline


rag = RAGPipeline()

question = "What is this software requirements specification?"

answer, sources = rag.ask(question)

print("\nAI Answer:")
print(answer)

print("\nSources:")

for source in sources:

    print(
        f"- {source['source']} "
        f"(Page {source['page']})"
    )