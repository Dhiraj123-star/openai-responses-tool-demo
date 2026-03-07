from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_service import ask_ai

app = FastAPI(title="OpenAI Tool Calling API")

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query:Query):
    result = ask_ai(query.question)
    return {"answer":result}