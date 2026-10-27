# Day 3 — Token Usage

## Topics

- Prompt, completion, and total token counts in an API response.
- The response's `finish_reason`.
- The relationship between prompt size, generated output, and usage.

The example defines three prompts and prints usage information from a chat
completion response. In the current script, the request is outside the loop, so
only the final prompt is sent. Move the request and usage reporting into the
loop if the intent is to measure all three prompts separately.

## Run

From this folder:

```powershell
uv sync
uv run python .\tokens.py
```

Set `GROQ_API_KEY` in a `.env` file in this folder first.

## Interview questions

**1. What is a token in a language model?**  
A token is a unit of text processed by the model. It may be a word, part of a
word, punctuation, or another text fragment.

**2. What is the difference between prompt and completion tokens?**  
Prompt tokens represent input messages; completion tokens represent generated
output. Total tokens are their combined usage.

**3. What does `finish_reason` tell you?**  
It indicates why generation ended, such as reaching a normal stopping point or
a configured output limit.

**4. Why monitor token usage?**  
It helps estimate usage and cost, detect unexpectedly large prompts or
responses, and manage model limits.