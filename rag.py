# rag.py
import faiss
import numpy as np
from openai import OpenAI

client = OpenAI()

documents = [
    "Order delivery takes 3-5 days",
    "Return policy is 7 days",
    "You can track order using order ID"
]

def get_embedding(text):
    res = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return res.data[0].embedding

embeddings = [get_embedding(doc) for doc in documents]
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings).astype("float32"))

def retrieve(query):
    q_embed = np.array([get_embedding(query)]).astype("float32")
    _, I = index.search(q_embed, k=2)
    return [documents[i] for i in I[0]]