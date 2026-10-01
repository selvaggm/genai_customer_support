from ollama import chat

print("1. Starting...")
print("2. Connecting to Ollama...")

response = chat(
    model="qwen3:latest",
    messages=[
        {
            "role": "user",
            "content": "What is an LLM? Answer in 2 lines."
        }
    ]
)

print("3. Response received")
print(response.message.content)