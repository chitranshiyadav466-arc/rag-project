from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
import pinecone
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Pinecone credentials
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENVIRONMENT")

# Initialize Pinecone
pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)

# Name of your index
index_name = "rag-demo"

# Load documents from 'data/' folder
documents = []
data_folder = "data"
for filename in os.listdir(data_folder):
    if filename.endswith(".txt"):
        loader = TextLoader(os.path.join(data_folder, filename))
        documents.extend(loader.load())

# Create embeddings
embeddings = OpenAIEmbeddings()  # Make sure OPENAI_API_KEY is in .env

# Upload to Pinecone
vectorstore = Pinecone.from_documents(documents, embeddings, index_name=index_name)

print("Documents uploaded to Pinecone successfully!")