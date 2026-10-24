import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing!")

client = Groq(api_key=api_key)

model = "openai/gpt-oss-120b"

def llm_ans(prompt):
    message={
        "role": "user",
        "content": prompt
    }

    messages = [message]
    response=client.chat.completions.create(model=model, messages=messages)
    ans = response.choices[0].message.content
    return ans

bad_prompt = """
#ROLE: 
you are a support assistant at a mobile/laptop company
#TASK:
you have to classify the issue in a category
#CONSTRAINT:
you have to classify the issue in one of three categories namely billing, technical, return
#OUTPUT FORMAT
your answer should be in one word only. the one word should be one of the categories given in constraints.
#EXAMPLE:
For instance if a user complain says he wants a refund then the category is return
#FALLBACK:
if the issue is unrelated to any of the categories mentioned in constraints, then the answer should be OTHER
This is a user complaint:
My laptop is not working
"""

print(llm_ans(bad_prompt))