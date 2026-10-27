import numpy as np
from sentence_transformers import SentenceTransformer
# from torch import cosine_similarity

def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Input text
text = "Machine learning is fun."

# Generate embedding
embedding = model.encode(text)

# Display results
""" print("Embedding shape:", embedding.shape)
print("Embedding:", embedding[10])
 """
# Ex
t1 = "There are 24 paid leaves";
t2 = "There are 24 vacation days";

v1 = model.encode(t1);
v2 = model.encode(t2);
print(cosine_similarity(v1, v2))
