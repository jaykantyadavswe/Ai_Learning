# Week 3, Day 3 — End-to-End RAG

## Topics

- Encoding a collection of policy documents and a user query.
- Ranking documents by cosine similarity and selecting the closest match.
- Supplying the retrieved document as context to the Groq chat completions API.

The example uses a Sentence Transformer for embeddings, NumPy for similarity,
and Groq for answer generation. It retrieves one document from a small
in-memory collection; it does not use a persistent vector database.

## Run

From this folder:

```powershell
uv sync
uv run python .\full_rag.py
```

Set `GROQ_API_KEY` in a `.env` file in this folder first.

## Interview questions

**1. What are the main stages in this RAG example?**  
Embed the documents, embed the query, find the most similar document, and send
the query with that document as context to the language model.

**2. Why embed the query with the same model as the documents?**  
Both vectors need to occupy a compatible embedding space so their similarity
can be meaningfully compared.

**3. What is top-k retrieval?**  
It selects the `k` highest-ranked results. This example returns only the single
highest-scoring document.

**4. What is one limitation of retrieving only one document?**  
The best single match may omit useful information found in other documents.
Retrieving several relevant passages can provide broader context, while still
requiring relevance and context-size checks.

**5. Does RAG eliminate hallucinations?**  
No. Retrieved context can improve grounding, but retrieval may be incomplete
and a model may still produce unsupported claims.