# Day 6 — Prompt Engineering

## Topics

- Defining a role, task, constraints, and output format in a prompt.
- Providing an example and a fallback category.
- Classifying a complaint into one of a fixed set of labels.

The script asks the model to classify a support complaint into `billing`,
`technical`, `return`, or the fallback `OTHER`.

## Run

From this folder:

```powershell
uv sync
uv run python .\prompt_engg.py
```

Set `GROQ_API_KEY` in a `.env` file in this folder first.

## Interview questions

**1. What makes a prompt useful for a classification task?**  
Clear labels, decision criteria, constraints, and a defined output format make
the expected result less ambiguous.

**2. Why include a fallback such as `OTHER`?**  
It gives the model an explicit response for inputs that do not fit any allowed
category.

**3. What is few-shot prompting?**  
It provides one or more examples in the prompt to demonstrate the desired
input-output behavior.

**4. Should an application trust the model to return only an allowed label?**  
No. Validate the response against the allowed set and handle unexpected output.
