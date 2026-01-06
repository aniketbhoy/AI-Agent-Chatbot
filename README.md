![Build Status](https://github.com/aniketbhoy/AI-Agent-Chatbot/actions/workflows/docker-publish.yml/badge.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/aniketbhoy74/ai-agent-chatbot)
![Docker Image Size](https://img.shields.io/docker/image-size/aniketbhoy74/ai-agent-chatbot)
---

# AI Agent Chatbot (LangChain · Groq · OpenAI · Tavily)

An end-to-end **AI Agent Chatbot** featuring a FastAPI backend and Streamlit frontend.
It supports multiple LLM providers, optional web search, and a clean, modular agent architecture.

---

## Overview

This project demonstrates how to build a modern AI agent using **LangChain**, with seamless switching between **Groq** and **OpenAI** models, optional **real-time web search**, and a user-friendly web interface.

---

## Features

* Switch between **Groq** and **OpenAI** providers
* Optional real-time web search via **Tavily**
* Custom system prompts
* Fast inference with **Groq**
* Modular, extensible agent design
* Interactive **Streamlit** UI
* Safety checks for model/provider compatibility

---

## Project Structure

```text
AI Agent Chatbot/
│
├── backend.py          # FastAPI server
├── ai_agent.py         # LangChain agent logic
├── frontend.py         # Streamlit UI
├── .env                # API keys (not committed)
├── requirements.txt
└── README.md
```

---

## Environment Setup

### Create a Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate   # macOS / Linux
# myenv\Scripts\activate    # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxx
OPENAI_API_KEY=sk_xxxxxxxxxxxxx
TAVILY_API_KEY=tvly_xxxxxxxxxxx
```

> **Note:** OpenAI requires an active billing quota.
> If your OpenAI quota is exhausted, use **Groq** instead.

---

## Running the Application

### Start the Backend (FastAPI)

```bash
uvicorn backend:app --host 127.0.0.1 --port 9999
```

Verify the server is running:

```text
Uvicorn running on http://127.0.0.1:9999
```

---

### Start the Frontend (Streamlit)

```bash
streamlit run frontend.py
```

Your browser will open automatically.

---

## Example API Request

```http
POST /chat
```

```json
{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "Groq",
  "system_prompt": "You are a helpful AI assistant",
  "messages": ["What are the latest crypto trends?"],
  "allow_search": true
}
```

---

## Supported Models

### Groq

* `llama-3.3-70b-versatile`

### OpenAI

* gpt-4o-mini`

### Blocked / Deprecated

* `mixtral-8x7b-32768`

---

## How It Works (High-Level)

```text
Streamlit UI
   ↓ HTTP POST
FastAPI Backend
   ↓
LangChain Agent
   ↓
Groq / OpenAI (+ Tavily Web Search)
```

---

## Tech Stack

* Python 3.12
* FastAPI
* Streamlit
* LangChain
* Groq
* OpenAI
* Tavily
* Uvicorn

---

## Project Status

* ✔ Backend stable
* ✔ Frontend fully functional
* ✔ Groq integration working
* ⚠ OpenAI requires active quota

---

## Future Improvements

* Chat history & memory
* Streaming responses
* Provider fallback logic
* Docker support
* Cloud deployment (AWS / Fly.io / Render)

---

## License

MIT License

---
