# Planner Service - Prompt-based Planning 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

generator = pipeline("text-generation", model="gpt2")

class SummaryInput(BaseModel):
    summary: str

@app.post("/plan/")
def generate_plan(data: SummaryInput):
    prompt = (
        "You are a project strategist. Based on the following meeting summary, create an action plan with assigned tasks and deadlines.\n\n"
        f"Meeting Summary:\n{data.summary}\n\nAction Plan:\n"
    )

    try:
        response = generator(prompt, max_length=150, num_return_sequences=1)
        return {"action_plan": response[0]["generated_text"].split("Action Plan:")[-1].strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
