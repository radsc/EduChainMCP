from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from educhain import Educhain
from openai import OpenAI

clientkey = OpenAI()

class ContentRequest(BaseModel):
    topic: str
    num_questions: Optional[int] = 5

# Initialize FastAPI app
app = FastAPI(title="EduChain MCP Server")

client = Educhain() # Deafault gpt-4o-mini Model

# Create /generate-questions endpoint
@app.post("/generate-questions")
async def generate_questions(req: ContentRequest):
    try:
        questions = client.qna_engine.generate_questions(topic=req.topic, num_questions=req.num_questions)
        return {"topic": req.topic, "questions": questions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create /generate-lesson-plan endpoint
@app.post("/generate-lesson-plan")
async def generate_lesson_plan(req: ContentRequest):
    try:
        lesson_plan = client.content_engine.generate_lesson_plan(topic=req.topic)
        return {"topic": req.topic, "lesson_plan": lesson_plan}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create a root route
@app.get("/")
async def root():
    return {"message": "EduChain MCP Server is running!"}

 
