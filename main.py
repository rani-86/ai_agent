from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

app = FastAPI()

# request schema
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