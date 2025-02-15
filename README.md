# Local RAG QA System

A question-answering system using RAG (Retrieval Augmented Generation) with local documents.

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```
Windows users:
```bash
set OPENAI_API_KEY="your-api-key-here"
```

3. Start the server:

Using Flask:
```bash
python rag_server.py
```

4. Access the application:
- Flask: Query http://localhost:8080 with CURL

Example request:
```bash
curl -X POST http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "what is the nearest location to berlin ostbahnhof?"}'
```

## Learn How to Build This

Watch the step-by-step tutorial:
[Building a Company Chatbot with Vector Stores & Similarity Search](https://www.ai-for-devs.com/products/latest-videos/categories/2157075237/posts/2185173154)

## Features

- Question answering using local documents
- Choice of web interfaces (FastAPI or Flask)
- Uses OpenAI's API for embeddings and completion
- Local document storage in `data/` directory
