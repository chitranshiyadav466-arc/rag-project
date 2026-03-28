
 # GaruanCDX RAG Chatbot
**Internal & Client-Facing Knowledge Assistant**
## Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot built using FastAPI and Mistral (via Ollama).
It answers user queries based strictly on uploaded documents (PDFs/text files) instead of generating random responses, ensuring high accuracy and reliability.
The system prevents hallucination by returning "Data not available" when relevant information is not found in the documents.
This chatbot is designed for:
Employee onboarding
Internal knowledge access
Client support systems

 ## Live Demo
Frontend: https://garuan-cdx-ai-chatbot-project-5cyd.vercel.app/
Backend: 

## Features
a)Document-based Question Answering
b)Semantic Search using RAG
c)No hallucination (returns “Data not available”)
d)FastAPI backend
e)Clean chatbot UI

## Tech Stack
- Frontend: React.js, Tailwind CSS
- Backend & Database: FastAPI (Python)
- AI: RAG pipeline with LLM
- Deployment: Vercel
- AI Model: Mistral via Ollama
Concept: Retrieval-Augmented Generation (RAG)

## How It Works
User asks a question
Relevant documents are retrieved
Context is passed to Mistral model
Model generates accurate answer

- 
## Run Locally
git clone https://github.com/chitranshiyadav466-arc/rag-project.git
cd rag-project
pip install -r requirements.txt
uvicorn main:app --reload

## Project Structure
rag-project/
│── data/        # Input files
│── docs/        # Documents
│── main.py      # FastAPI app
│── Rag.py       # RAG logic
│── README.md

 ## Team members
- **Naresh** – Backend & Project Management (Team Leader)
- **Chitranshi** – Backend Support
- **Abhishek** – Frontend & Integration

