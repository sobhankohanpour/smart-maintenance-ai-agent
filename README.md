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
````

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
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

## Installation

Ensure you have Python 3.13 installed. Then install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file in the root directory:

```text
OPENAI_API_KEY=your_openai_api_key_here
```

2. Make sure your `.gitignore` excludes the `.env` file to keep your API key safe.

## Usage

Run the CLI to interact with the agent:

```bash
python src/main.py
```

Example input:

```
Welcome to Smart Maintenance AI Agent!
Describe the maintenance issue: The air conditioning is not cooling properly in the office.
```

The agent will return a structured maintenance plan as JSON:

```json
{
    "issue_type": "HVAC",
    "priority": "High",
    "risk": "Medium",
    "recommended_actions": ["Check thermostat", "Inspect AC unit", "Clean filters"],
    "assigned_vendor": "HVAC Team A",
    "estimated_response_time": "2 hours"
}
```

## Dependencies

* `openai` for LLM integration
* `pydantic` for structured output validation
* `python-dotenv` for loading environment variables

## Notes

* All AI outputs conform to the `MaintenanceTask` schema (`schemas.py`)
* The agent uses `prompts.py` for prompt templates and `tools.py` for helper functions
* Current LLM model: `gpt-3.5-turbo` (update your quota in OpenAI if you encounter errors)

## License

MIT License

