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
├── src/
│   ├── agent.py        # Core AI agent logic
│   ├── tools.py        # Tool functions
│   ├── schemas.py      # Pydantic models
│   ├── prompts.py      # Prompt templates
│   └── main.py         # Entry point
│
├── tests/
├── requirements.txt
├── README.md
├── .env
└── .gitignore


```

## How to use

python 3.13

```bash
pip install -r requirements.txt
```