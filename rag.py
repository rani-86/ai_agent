# rag.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Order delivery takes 3-5 days",
    "Return policy is 7 days",
    "You can track order using order ID"
]

vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

def retrieve(query):
    q_vec = vectorizer.transform([query])
    sims = cosine_similarity(q_vec, doc_vectors)[0]
    top_idx = sims.argsort()[-2:][::-1]  # top 2 matches
    return [documents[i] for i in top_idx]
