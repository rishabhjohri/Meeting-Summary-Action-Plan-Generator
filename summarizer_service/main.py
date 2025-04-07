# Summarizer Service - T5 Inference 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

summarizer = pipeline("summarization", model="t5-small")  # or "facebook/bart-large-cnn"

class TextInput(BaseModel):
    text: str

@app.post("/summarize/")
def summarize_text(data: TextInput):
    try:
        result = summarizer(data.text, max_length=100, min_length=30, do_sample=False)
        return {"summary": result[0]["summary_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
