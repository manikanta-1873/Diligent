import os
from langchain_community.llms import Ollama
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from pinecone import Pinecone

# -----------------------------
# Pinecone Client (NEW WAY)
# -----------------------------
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

INDEX_NAME = "jarvis-index"

# Connect to index (assumes index already exists)
index = pc.Index(INDEX_NAME)

# -----------------------------
# Embeddings
# -----------------------------
embeddings = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# -----------------------------
# Vector Store
# -----------------------------
vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

# -----------------------------
# Ollama LLM
# -----------------------------
llm = Ollama(model="tinyllama")

# -----------------------------
# Functions
# -----------------------------
def add_knowledge(text):
    docs = [Document(page_content=text)]
    vectorstore.add_documents(docs)

def ask_jarvis(query):
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are Jarvis, a knowledgeable AI assistant similar to ChatGPT.

Answer the user's question clearly, directly, and informatively.
Do NOT introduce yourself.
Do NOT talk about being an AI.
Do NOT add filler or meta commentary.

If relevant context is provided, use it.
Otherwise, answer from general knowledge.

Context:
{context}

User question:
{query}

Final answer:
"""

    response = llm.invoke(prompt)

    # Return clean response
    return response.strip()




