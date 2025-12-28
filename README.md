# Smart Maintenance AI Agent (Mini Version)

Smart Maintenance AI Agent is a lightweight, end-to-end AI agent designed to automate property maintenance requests. It analyzes user-reported issues, classifies intent and priority, generates actionable plans, and assigns the appropriate vendor using LLM reasoning and structured outputs. 

## Project Architecture 

```text
User Input
   ↓
LLM (Reasoning + Classification)
   ↓
Tool Calls (Python Functions)
   ↓
Action Plan (JSON)
   ↓
Final Response

```

## Project Structure

```
smart-maintenance-ai-agent/
│
├── app/
│   ├── agent.py          # Logic of the AI Agent
│   ├── tools.py          # Tool functions (vendor selection, priority, ...)
│   ├── schemas.py        # Pydantic models (structured output)
│   └── prompts.py        # Prompt templates
│
├── main.py               # Entry point (CLI or Streamlit)
├── requirements.txt
├── README.md
└── .env                  # API Keys (not committed)

```

## How to use

python 3.13
