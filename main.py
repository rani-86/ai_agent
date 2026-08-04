import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from agent import agent

# Load environment variables
load_dotenv()

# 1. Initialize FastAPI FIRST
app = FastAPI()

# 2. Mount static directory and setup static routes AFTER initializing app
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

# Request schema
class Query(BaseModel):
    user_id: str
    message: str

# API route
@app.post("/chat")
def chat(query: Query):
    response = agent(query.user_id, query.message)
    return {
        "user_id": query.user_id,
        "response": response
    }
    return {
        "user_id": query.user_id,
        "response": response
    }
