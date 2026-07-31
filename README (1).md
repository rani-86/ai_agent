# AI Customer Support Agent (RAG)

An AI-powered customer support chatbot that uses Retrieval-Augmented Generation (RAG) to answer domain-specific queries, backed by a fast open-source LLM (via Groq) and a lightweight TF-IDF retrieval pipeline.

**Live Demo:** _[add your Render URL here once deployed]_
**Repo:** https://github.com/rani-86/ai_agent

---

## Features

- **RAG-based responses** — retrieves relevant context from a knowledge base before generating an answer, so replies are grounded rather than hallucinated.
- **Fast LLM inference** — powered by Groq's API running Llama 3.3, no paid API key required.
- **Conversational memory** — maintains per-user chat history across a session.
- **Tool integration** — detects order-related queries and looks up order status via a simple tool call.
- **REST API** — built with FastAPI, exposing a single `/chat` endpoint.
- **Web chat UI** — minimal HTML/JS frontend served directly by FastAPI.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| LLM | Groq API (Llama 3.3 70B) |
| Retrieval | Scikit-learn (TF-IDF + cosine similarity) |
| Memory | In-memory per-user store |
| Deployment | Render (free tier) |

---

## Project Structure

```
ai_agent/
├── main.py          # FastAPI app and /chat endpoint
├── agent.py         # Core agent logic — combines RAG context, memory, and tool output into a prompt
├── rag.py           # TF-IDF based document retrieval
├── memory.py        # Per-user conversational memory store
├── tools.py         # Example tool: order status lookup
├── requirements.txt # Python dependencies
├── static/
│   └── index.html   # Simple chat UI
└── runtime.txt       # Pinned Python version for deployment
```

---

## How It Works

1. A user sends a message to `POST /chat` with their `user_id` and `message`.
2. `agent.py` retrieves relevant context from the knowledge base (`rag.py`), pulls prior conversation history (`memory.py`), and checks if the message needs a tool call (`tools.py`, e.g. order status lookups).
3. All of this is combined into a single prompt and sent to the Groq LLM.
4. The response is returned to the user and saved to memory for context in future turns.

---

## Getting Started

### Prerequisites
- Python 3.11+
- A free Groq API key from [console.groq.com](https://console.groq.com)

### Setup

```bash
git clone https://github.com/rani-86/ai_agent.git
cd ai_agent
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

### Run locally

```bash
uvicorn main:app --reload
```

Visit `http://localhost:8000` for the chat UI, or send requests directly to `http://localhost:8000/chat`.

### Example request

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user1", "message": "What is your return policy?"}'
```

---

## Deployment

This project is deployed on [Render](https://render.com) (free tier).

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Environment variable required:** `GROQ_API_KEY`

> Note: Render's free tier spins down after inactivity, and in-memory conversation history resets on restart.

---

## Future Improvements

- Persist conversational memory using a database (e.g. Supabase/Postgres or Redis) instead of an in-memory dict
- Expand the knowledge base with real support documents
- Add authentication for the API
- Add response streaming for a more responsive chat experience

---

## License

MIT
