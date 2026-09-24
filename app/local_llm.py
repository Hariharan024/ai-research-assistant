from ollama import chat


class LocalLLM:

    def generate(self, question, context, chat_history):

        history_text = ""

        for message in chat_history:

            history_text += (
                f"User: {message['question']}\n"
                f"AI: {message['answer']}\n\n"
            )

        prompt = f"""
You are an AI research assistant.

Answer the user's question using the provided document context
and conversation history.

If the answer is not available in the document context,
say that the information is not available in the provided document.

Conversation History:
{history_text}

Document Context:
{context}

Current Question:
{question}
"""

        response = chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]