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

JD = """
We are hiring a Backend Python Developr.

Requirements:
-   Strong Python
-   FastAPI or Django
-   PostgreSQL
-   Docker
-   AWS
-   REST APIs
-   2+ years of experience
"""

RESUME="""
Name: Rahul Sharma

Experience:
3 years as a Software Developer.

Skills:
Python, FastAPI, MySQL, Docker,
REST APIs, Git

Projects:
Built a food delivery backend using
FastAPI and MySQL.

Deployed applications using Docker.
"""

def ask_llm(system_prompt, user_prompt):
    print("step1")
    sys_msg={
        "role": "system",
        "content": system_prompt
    }
    
    user_msg={
        "role": "user",
        "content": user_prompt
    }

    messages=[sys_msg, user_msg]

    response=client.chat.completions.create(model=model, messages=messages)
    answer=response.choices[0].message.content
    return answer

def step1_res_extract(RESUME):
    print("step2")
    #extract skills from resume
    system_prompt="""
    you are a professional HR assistant. Extract the skills from the candidates resume provided.
    Only return the skills no other information. Do not invent any skills by yourself.
    Output format:
    Skills should be separated by commas. Just return commas seprated skills do not return any other filler information.
    """

    user_prompt=f"""
    Extract the skills from this resume
    {RESUME}
    """
    return ask_llm(system_prompt, user_prompt)

def step2_JD_extract(JD):
    print("step3")

    #extract skills from JD
    system_prompt="""
    you are a professional HR assistant. Extract the skills from the Job description provided.
    Only return the skills no other information. Do not invent any skills by yourself.
    Output format:
    Skills should be seprated by commas. Just return commas seprated skills do not return any other filler information
    """

    user_prompt=f"""
    Extract the skills from this resume
    {JD}
    """
    return ask_llm(system_prompt, user_prompt)

def step3_match(candidate, JD):
    print("step4")
    system_prompt="""
    you are a professional HR assistant. compare the skills of condidate and the skills required in the JD and produce a final score between 1 and 100.
    also produce a short verdict whether the candidate is a good fit for the role.
    """

    user_prompt=f"""
    Compare and match the skills
    JD:
    {JD}
    candidate:
    {candidate}
    """
    return ask_llm(system_prompt, user_prompt)

candidate = step1_res_extract(RESUME)
print(candidate)
sleep(2)
jd = step2_JD_extract(JD)
print(jd)
sleep(2)
score = step3_match(candidate, jd)
print(score)