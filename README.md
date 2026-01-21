# 🤖 Jarvis – AI Assistant (Diligent Placement Assignment)

## Overview
Jarvis is a self-hosted AI assistant built for the Diligent placement assignment. It uses a locally running Large Language Model (LLM) integrated with a vector database to deliver clear, GPT-like conversational responses through a chatbot interface.

The system follows a Retrieval-Augmented Generation (RAG) architecture and demonstrates how enterprise knowledge can be stored, retrieved, and used to answer user queries contextually.

## Key Features
- Self-hosted AI assistant (Jarvis)
- GPT-style conversational responses
- Knowledge storage and retrieval using a vector database
- Retrieval-Augmented Generation (RAG)
- Clean and minimal chatbot UI
- Secure handling of API keys using environment variables

## Tech Stack
- LLM: TinyLLaMA (via Ollama – self-hosted)
- Vector Database: Pinecone
- Framework: LangChain
- UI: Streamlit
- Programming Language: Python

## Architecture
User Query → Streamlit Chat UI → Context Retrieval (Pinecone Vector DB) → Ollama (TinyLLaMA – Local LLM) → Final Answer

## How It Works
1. Users add enterprise knowledge through the UI.
2. Knowledge is converted into vector embeddings and stored in Pinecone.
3. When a user asks a question, relevant context is retrieved from Pinecone.
4. The local LLM (TinyLLaMA) generates a direct, human-like response.
5. Only the final answer is shown to the user with no explanations or labels.

## Output Behavior
- Input: User query
- Output: Only the final answer
- No repeated questions
- No reasoning or system messages
- Clean, ChatGPT-style responses

## How to Run the Project
Install dependencies:
pip install -r requirements.txt

Run the local LLM:
ollama run tinyllama

Start the application:
streamlit run app.py

## Security Best Practices
- Pinecone API key is managed using environment variables
- No API keys are hardcoded
- Safe for public GitHub repositories

## Why TinyLLaMA?
TinyLLaMA was chosen to keep inference lightweight and fast during development while maintaining compatibility with larger LLaMA models. The architecture can be easily scaled to stronger models such as LLaMA-3 without code changes.

## Conclusion
This project demonstrates an enterprise-ready AI assistant using a self-hosted LLM, vector-based knowledge retrieval, and a conversational chatbot UI, reflecting real-world AI system design used in modern SaaS products.

Author: Mani Kanta  
Repository: https://github.com/manikanta-1873/Diligent
