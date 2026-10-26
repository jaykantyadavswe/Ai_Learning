
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

# Step1
knowledge_base = {
    "Name": "Jaykant yadav",
    "work": "It is a software engg. and also content creator",
    "age": 22,
    "networth": "Billions"
}

# Step2 retreieval


def retrieve_info(question):
    question = question.lower()
    if "age" in question:
        return knowledge_base["age"]
    elif "networth" in question:
        return knowledge_base["networth"]
    elif "work" in question:
        return knowledge_base["work"]
    elif "Name" in question:
        return knowledge_base["Name"]
    else:
        return None


def ask_llm(question):
    context = retrieve_info(question)
    system_prompt = f"""Answer only one line, answer in only based on this context. do not hallucinae. Context: {context}"""

    system_message = {
        "role": "system",
        "content": system_prompt
    }

    message = {
        "role": "user",
        "content": question
    }

    messages = [system_message, message]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    answer = response.choices[0].message.content
    return answer


question = "What is age of Jaykant yadav"

res = ask_llm(question)
print(res)
