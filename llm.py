from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2:1b', messages=[
    {"role": "system", "content": "You are a helpful assistant running on a Raspberry Pi device. Your name is Llama."},
    {"role": "user", "content": "What is your name?"},
])
print(response.message.content)