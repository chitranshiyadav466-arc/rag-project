from langchain_community.llms import Ollama
import os

# Load Ollama model
llm = Ollama(model="mistral")

#Global context (will refresh when new files uploaded)
context_data = ""

# STEP 1: Load all documents
def load_documents():
    global context_data
    context_data = ""

    docs_path = "docs"

    for filename in os.listdir(docs_path):
        file_path = os.path.join(docs_path, filename)

        if filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                context_data += file.read() + "\n"

# STEP 2: Refresh index (called after upload)
def refresh_index():
    load_documents()

# STEP 3: Get answer using Ollama
def get_answer(question: str):
    global context_data

    # If no data loaded yet
    if not context_data:
        load_documents()

    #  Prompt
    prompt = f"""
You are a helpful assistant.

Use ONLY the context below to answer.

Context:
{context_data}

Question: {question}

Answer:
"""

    #  Call Ollama
    response = llm.invoke(prompt)

    return response