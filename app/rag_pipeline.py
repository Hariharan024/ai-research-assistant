from app.vector_store import VectorStore
from app.local_llm import LocalLLM
from app.query_rewriter import QueryRewriter


class RAGPipeline:

    def __init__(self):

        self.vector_store = VectorStore()
        self.llm = LocalLLM()
        self.query_rewriter = QueryRewriter()

        # Conversation memory
        self.chat_history = []

    def ask(self, question, source=None):

        # Step 1: Rewrite the question using conversation history
        search_question = self.query_rewriter.rewrite(
            question,
            self.chat_history
        )



        # Step 2: Retrieve relevant document chunks
        results = self.vector_store.search(
            search_question,
            top_k=3,source=source
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        # Step 3: Build document context
        context_parts = []

        for document, metadata in zip(documents, metadatas):

            source = metadata["source"]
            page = metadata["page"]

            context_parts.append(
                f"[Source: {source}, Page: {page}]\n"
                f"{document}"
            )

        context = "\n\n".join(context_parts)

        # Step 4: Generate answer
        answer = self.llm.generate(
            question,
            context,
            self.chat_history
        )

        # Step 5: Save conversation
        self.chat_history.append({
            "question": question,
            "answer": answer
        })

        return answer, metadatas
