from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
import os

app = FastAPI()

# Allow frontend or other services to call this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(('.txt', '.pdf')):
        raise HTTPException(status_code=400, detail="Only .txt or .pdf files are allowed.")

    contents = ""
    
    if file.filename.endswith('.txt'):
        contents = (await file.read()).decode('utf-8')
    
    elif file.filename.endswith('.pdf'):
        try:
            temp_path = f"temp_{file.filename}"
            with open(temp_path, "wb") as f:
                f.write(await file.read())
            
            reader = PdfReader(temp_path)
            for page in reader.pages:
                contents += page.extract_text() or ""
            
            os.remove(temp_path)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"PDF parsing failed: {str(e)}")

    return {"text": contents.strip()}
# Upload Service - FastAPI + PDF/Text Parser 
