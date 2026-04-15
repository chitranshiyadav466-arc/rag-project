from fastapi import FastAPI, UploadFile, File
import shutil
import os
from Rag import get_answer, refresh_index

app = FastAPI()

# Ensure docs folder exists
os.makedirs("docs", exist_ok=True)

# STEP 1: Ask question (uses RAG + Ollama inside Rag.py)
@app.get("/ask")
def ask(question: str):
    try:
        answer = get_answer(question)

        return {
            "question": question,
            "answer": answer
        }
    
    except Exception as e:
        return {
            "question": question,
            "answer": f"Error: {str(e)}"
        }


# STEP 2: Upload document
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    try:
        file_path = os.path.join("docs", file.filename)
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Refresh RAG index
        refresh_index()
        
        return {
            "message": "File uploaded and index updated successfully",
            "filename": file.filename
        }

    except Exception as e:
        return {
            "message": f"Upload failed: {str(e)}"
        }


# STEP 3: Health check (optional but useful)
@app.get("/")
def home():
    return {"message": "RAG API is running "}