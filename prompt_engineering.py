from ollama import chat

response = chat(
    model="qwen3:latest",
    messages=[
        {
            "role": "system",
            "content": """
You are an AI customer support assistant.

Rules:
1. Be professional and helpful.
2. Give simple and clear answers.
3. If you don't know the answer, say you don't know.
4. Do not invent company policies.
"""
        },
        {
            "role": "user",
            "content": "My order has not arrived yet. What should I do?"
        }
    ]
)

print(response.message.content)