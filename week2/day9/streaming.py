import os
import re
from time import sleep
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing!")

client = Groq(api_key=api_key)

model = "openai/gpt-oss-120b"

prompt = "Explain how to create content?"

messsage={
    "role": "user",
    "content": prompt
}

messsages = [messsage]

stream = client.chat.completions.create(model=model, messages=messsages, stream=True)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)