import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from agent import agent

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
async def chat(query: Query):
    return StreamingResponse(
        agent(query.user_id, query.message),
        media_type="text/plain"
    )
