# rag.py
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Order delivery takes 3-5 days",
    "Return policy is 7 days",
    "You can track order using order ID"
]

def get_embedding(text):
    return embedder.encode(text)

embeddings = [get_embedding(doc) for doc in documents]
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings).astype("float32"))

def retrieve(query):
    q_embed = np.array([get_embedding(query)]).astype("float32")
    _, I = index.search(q_embed, k=2)
    return [documents[i] for i in I[0]]
