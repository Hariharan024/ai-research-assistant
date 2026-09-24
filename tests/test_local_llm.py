from app.local_llm import LocalLLM


llm = LocalLLM()

answer = llm.generate(
    "What is machine learning?",
    "Machine learning allows computers to learn patterns from data."
)

print(answer)