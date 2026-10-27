# Day 8 — Prompt Chaining

## Topics

- Breaking a task into sequential LLM calls.
- Extracting skills from a resume and a job description separately.
- Comparing extracted information in a final matching step.

The example has three stages: candidate skill extraction, job requirement
extraction, and a match score with a short verdict. Each stage's output becomes
input to the next stage.

## Run

From this folder:

```powershell
uv sync
uv run python .\prompt_chaining.py
```

Set `GROQ_API_KEY` in a `.env` file in this folder first.

## Interview questions

**1. What is prompt chaining?**  
It is a workflow in which outputs from one prompt or model call are passed to
later steps to complete a larger task.

**2. Why split resume matching into multiple steps?**  
Separate extraction and comparison tasks can make intermediate results easier
to inspect and each prompt easier to specify.

**3. What is a drawback of chaining multiple model calls?**  
It increases latency and API usage, and an error in an early step can affect
every later step.

**4. How can you make a matching score more reliable?**  
Use explicit criteria, preserve evidence from the source documents, validate
the output, and have a human review the assessment.
