# Week 3, Day 2 — Embeddings and Cosine Similarity

## Topics

- Encoding text with the `all-MiniLM-L6-v2` Sentence Transformer.
- Representing sentences as numerical vectors called embeddings.
- Comparing two embeddings using cosine similarity.

The example compares two differently worded sentences about paid leave. The
similarity score indicates how aligned their embedding vectors are; it is not
a probability that the sentences are equivalent.

## Run

From this folder:

```powershell
uv sync
uv run python .\embed_rag.py
```

## Interview questions

**1. What is a text embedding?**  
It is a numerical vector representation of text that captures information
useful for comparing its meaning or use.

**2. What does cosine similarity measure?**  
It measures the cosine of the angle between two vectors. A larger value
generally indicates more similar vector directions.

**3. Why use embeddings instead of exact keyword matching?**  
Embeddings can identify semantic similarity even when two texts use different
words, while exact matching depends more directly on shared terms.

**4. Is cosine similarity a calibrated confidence score?**  
No. It is a vector similarity measure; its interpretation depends on the model,
data, and application threshold.