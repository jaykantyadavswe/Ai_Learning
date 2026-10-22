
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing!")

client = Groq(api_key=api_key)

model = "openai/gpt-oss-120b"


# Structure It
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str
    contact:str

schema=Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}

system_prompt=f"""
System the personal information from the ticket strictly based on this schema and give a json output.
{schema}
 """

message_system = {
    "role": "system",
    "content": system_prompt
}
text = "Hello my name is Jaykant. I have an iphone whice is not working at all. my address is delhi. my email is abc@gmail.com. my contact number is 8202455329"

prompt = f"""
This is a custemer ticket. please extract the personal information from this.
{text}
"""

role = "user"
# prompt = "Suggest a name for my food company";

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
    temperature=0,
    response_format=response_format
)
# temprature by default is 0 meaning safe [0-2]
answer = response.choices[0].message.content
print(answer)

# Reading 
import json
raw_json = answer
data_file=json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
print(ticket.contact)
