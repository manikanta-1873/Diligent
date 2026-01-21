# 🤖 Jarvis – AI Assistant (Diligent Assignment)

## Overview
This project implements a self-hosted AI assistant (Jarvis) using Ollama and Pinecone.
It supports contextual question answering using vector-based retrieval and a chatbot UI.

## Tech Stack
- LLM: Ollama (tinyllama)
- Vector Database: Pinecone
- Framework: LangChain
- UI: Streamlit

## Architecture
User Query → Embedding → Pinecone Retrieval → Context → Ollama → Response

## How to Run
```bash
pip install -r requirements.txt
ollama run llama3
streamlit run app.py
