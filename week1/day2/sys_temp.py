
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing!")

client = Groq(api_key=api_key)

model = "openai/gpt-oss-120b"

message_system = {
    "role": "system",
    "content": "You are a brand manager who suggest name for my food company. name should be in one word, suggest one name only"
}

role = "user"
prompt = "Suggest a name for my food company";

# A dictionary, not a list
message = {
    "role": role,
    "content": prompt
}

# A list of dictionaries
messages = [message_system, message]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1
)
# temprature by default is 0 meaning safe [0-2]

print(response.choices[0].message.content)
