import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from agent import agent

load_dotenv()

app = FastAPI()

# Mount static files under /static
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

class Query(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
def chat(query: Query):
    response = agent(query.user_id, query.message)
    return {
        "user_id": query.user_id,
        "response": response
    }
