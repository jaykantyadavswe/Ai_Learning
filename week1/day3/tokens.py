
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing!")

client = Groq(api_key=api_key)

model = "openai/gpt-oss-120b"

""" message_system = {
    "role": "system",
    "content": "You are a brand manager who suggest name for my food company. name should be in one word, suggest one name only"
} """
# 3 Prompt
prompt1 = "Hi"
prompt2 = "Explain how to create content"
prompt3 = "How to brand my self"

prompts = [prompt1, prompt2, prompt3]
    


# A dictionary, not a list
for prompt in prompts:
    message = {
    "role": "user",
    "content": prompt
}

messages = [message]
response = client.chat.completions.create(model=model, messages=messages, max_tokens=500)
usage = response.usage
print(f"Prompt: {prompt} --> your token: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total_tokens: {usage.total_tokens} finish_reason: {response.choices[0].finish_reason}")


