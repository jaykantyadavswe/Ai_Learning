# Day 9 — Streaming Responses

## Topics

- Requesting a streamed chat completion.
- Processing response chunks as they arrive.
- Printing content incrementally rather than waiting for the full response.

## Run

From this folder:

```powershell
uv sync
uv run python .\streaming.py
```

Set `GROQ_API_KEY` in a `.env` file in this folder first.

## Interview questions

**1. What is response streaming?**  
It delivers generated output incrementally as chunks instead of returning the
complete response only after generation ends.

**2. What is a benefit of streaming in a user interface?**  
The user can see the response begin sooner, improving perceived responsiveness
for longer generations.

**3. What does a streaming chunk contain?**  
It may contain a delta with newly generated content, rather than a complete
message. Some chunks may not contain text.

**4. What should an application consider when handling a stream?**  
It should handle empty chunks, errors, cancellation, and completion, and avoid
assuming every chunk contains user-visible text.
