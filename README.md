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

3. Run the app:
```bash
uvicorn app:app --reload
```

4. Visit http://localhost:8000 in your browser

## Learn How to Build This

Watch the step-by-step tutorial:
[Building a Company Chatbot with Vector Stores & Similarity Search](https://www.ai-for-devs.com/products/latest-videos/categories/2157075237/posts/2185173154)
