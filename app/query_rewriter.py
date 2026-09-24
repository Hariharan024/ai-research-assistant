from ollama import chat


class QueryRewriter:

    def rewrite(self, question, chat_history):

        if not chat_history:
            return question

        history_text = ""

        for message in chat_history[-4:]:

            history_text += (
                f"User: {message['question']}\n"
                f"AI: {message['answer']}\n\n"
            )

        prompt = f"""
Rewrite the user's latest question so that it is
completely understandable on its own.

Use the conversation history to understand words such as:
"it", "this", "that", "they", "those", etc.

Do not answer the question.

Return only the rewritten question.

Conversation History:
{history_text}

Latest Question:
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

        return response["message"]["content"].strip()