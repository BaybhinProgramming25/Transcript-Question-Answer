# TQA — Transcript Q&A

TQA is a web application that lets Stony Brook CS students upload their academic transcripts as PDFs and ask natural language questions about their records. It uses a RAG (Retrieval-Augmented Generation) pipeline backed by OpenAI to answer questions accurately from the transcript content.

## Features

- Upload a PDF transcript and have it parsed and indexed automatically
- Ask natural language questions — "What's my GPA?", "What classes did I take this semester?", "What was my GPA during this semester?"
- Export your transcript to a formatted Excel (.xlsx) file
- Persistent chat history per document
- JWT-authenticated sessions with rate limiting

## Tech Stack

**Frontend & Backend**
- React 
- FastAPI (Python)
- SQLAlchemy + MySQL
- FAISS vector store for semantic search
- LangChain + OpenAI (`gpt-4o-mini`, `text-embedding-3-large`)

**Infrastructure**
- Docker + Docker Compose
- nginx (host) for SSL termination and reverse proxying
- Let's Encrypt for HTTPS


## Begin Using

Visit www.transcriptqa.org, see the sample PDF that is on the homepage, make an account, and begin asking questions! 