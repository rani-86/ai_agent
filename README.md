# AI Customer Support Agent (RAG)

An intelligent, lightweight customer support assistant built with **FastAPI**, **Groq (Llama 3.3)**, and **Scikit-learn**. It uses Retrieval-Augmented Generation (RAG) with TF-IDF similarity search to deliver grounded, context-aware answers to user queries with per-session multi-turn memory.

🚀 **[Live Demo](https://ai-agent-ey0o.onrender.com)** | 📁 **[GitHub Code](https://github.com/rani-86/ai_agent)**

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI, Uvicorn
* **LLM Engine:** Groq API (`llama-3.3-70b-versatile`)
* **Retrieval / Vector Engine:** Scikit-learn (TF-IDF Vectorizer + Cosine Similarity)
* **Frontend:** HTML5, Modern Dark CSS, Vanilla JavaScript
* **Deployment:** Render (Free Tier)

---

## 📋 Prerequisites

* Python 3.9+
* A free **Groq API Key** from [console.groq.com](https://console.groq.com/)

---

## ⚙️ Installation & Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Configure environment variables:**

Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

3. **Start the server:**
```bash
uvicorn main:app --reload
```

4. **Access the application:**
* Open [http://localhost:8000](http://localhost:8000) in your browser for the interactive web chat UI.
* View interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

---

## 🔌 API Usage

**Endpoint:** `POST /chat`

**Example Request (cURL):**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user1", "message": "What is your return policy?"}'
```

**Example Response:**
```json
{
  "user_id": "user1",
  "response": "Our standard return policy is 7 days..."
}
```

---

## ☁️ Deployment (Render)

This application is deployed as a Web Service on Render.

* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
* **Environment Variable:** `GROQ_API_KEY`

> **Note:** On Render's free tier, the web service spins down after 15 minutes of inactivity. Cold starts may take ~30 seconds, and in-memory chat session history resets upon restart.

---

## 🔮 Future Enhancements

* [ ] Persist conversation memory using Redis or PostgreSQL.
* [ ] Support dynamic knowledge base expansion from external JSON/Markdown files.
* [ ] Add Server-Sent Events (SSE) for real-time streaming responses.
* [ ] Implement API rate limiting and token-based authentication.

---

## 📜 License

Distributed under the MIT License.

