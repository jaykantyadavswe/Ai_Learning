# Day 2 — Roles and Temperature

## Topics

- Structuring a chat request with system and user messages.
- Using a system message to guide the model's role and output constraints.
- Setting the `temperature` parameter.

The example asks the model to suggest a one-word food-company name. Temperature
influences response variability; it does not guarantee correctness or a
particular output format.

## Run

From this folder:

```powershell
uv sync
uv run python .\sys_temp.py
```

Set `GROQ_API_KEY` in a `.env` file in this folder first.

## Interview questions

**1. What is the purpose of a system message?**  
It provides high-level instructions that guide how the model should respond.

**2. How is a system message different from a user message?**  
A system message defines behavior or constraints, while a user message provides
the request or input to answer.

**3. What does temperature control?**  
It adjusts the randomness of token selection. Lower values tend to produce
more consistent answers; higher values can produce more varied answers.

**4. Does a low temperature make a response factually correct?**  
No. It can make outputs more consistent, but accuracy still depends on the
model, prompt, and available information.
