# Week 3, Day 1 — Introductory Retrieval

## Topics

- Keeping a small knowledge base in Python.
- Selecting context with keyword-based retrieval.
- Passing the retrieved context to an LLM to answer a question.

This is a simple retrieval-augmented generation example: `retrieve_info`
chooses a value from the in-memory knowledge base, then the Groq model receives
that context with the question. Retrieval is based on explicit keyword checks,
not semantic similarity.

## Run

From this folder:

```powershell
uv sync
uv run python .\rag_intro.py
```

Set `GROQ_API_KEY` in a `.env` file in this folder first.

## Interview questions

**1. What is retrieval-augmented generation (RAG)?**  
RAG retrieves relevant information from an external knowledge source and
provides it to a language model as context for generating an answer.

**2. How does this example retrieve information?**  
It checks for specific keywords in the lowercased question and returns a
corresponding value from a Python dictionary.

**3. What is a limitation of keyword-based retrieval?**  
It can miss relevant questions phrased with different words and can match
keywords without understanding their meaning.

**4. Why provide retrieved context to the model?**  
It grounds the answer in supplied information and can reduce unsupported
responses, though it does not guarantee that the model will always follow it.