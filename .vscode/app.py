from fastapi import FastAPI, Query
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import pinecone

# Load environment variables from .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENVIRONMENT")
INDEX_NAME = "rag-demo"

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

# Load existing index
vectorstore = Pinecone.from_existing_index(INDEX_NAME, embedding=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))

# Create FastAPI app
app = FastAPI(title="RAG Project API", description="Query your documents using RAG model", version="1.0")

@app.get("/query")
def query(q: str = Query(..., description="Your question")):
    """
    Query your RAG index with a question.
    Returns a list of relevant document contents.
    """
    retriever = vectorstore.as_retriever()
    results = retriever.get_relevant_documents(q)
    return {
        "query": q,
        "results": [doc.page_content for doc in results]
    }