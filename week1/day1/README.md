# Day 1 — First Groq Chat Completion

## Topics

- Sending a user message to the Groq chat completions API.
- Creating a `Groq` client with an API key loaded from `.env`.
- Selecting a model and reading the assistant's response.

The script asks the model a simple question and prints its answer. Keep API
keys in `.env`; do not commit them to source control.

## Run

From this folder, install the locked dependencies and run:

```powershell
uv sync
uv run python .\hello.llm.py
```

Set `GROQ_API_KEY` in a `.env` file in this folder first.

## Interview questions

**1. What is a chat completion?**  
It is a model-generated response based on a sequence of messages supplied to a
chat model.

**2. Why does the request use a list of messages?**  
The list represents the conversation. Each message has a role, such as `user`
or `assistant`, and content.

**3. Why load an API key from an environment variable?**  
It separates credentials from source code, reducing the risk of accidentally
committing or sharing a secret.

**4. How does the script get the generated answer?**  
It reads the first choice's message content from the response object.
