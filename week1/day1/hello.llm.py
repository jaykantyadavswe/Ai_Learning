
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get the API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing!")

# Create the Groq client
client = Groq(api_key=api_key)

# Select the AI model
model = "openai/gpt-oss-120b"

# Ask a question
messages = [
    {
        "role": "user",
        "content": "Do you know Virat Kohli?"
    }
]

# Send the request to the AI
response = client.chat.completions.create(
    model=model,
    messages=messages
)

# Print only the AI's answer
print(response.choices[0].message.content)
