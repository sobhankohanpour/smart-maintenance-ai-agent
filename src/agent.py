"""
agent.py

Purpose:
    Handle communication with the LLM, implement decision-making logic, 
    use helper tools, and produce structured outputs.

Description:
    This module defines the main AI Agent workflow:
    - Receives a user issue
    - Sends a prompt to the LLM (OpenAI GPT-4)
    - Parses the JSON response
    - Enriches the response using helper functions (tools.py)
    - Returns a structured MaintenanceTask object

Dependencies:
    - schemas.py: Defines the MaintenanceTask Pydantic model
    - prompts.py: Contains the main LLM prompt templates
    - tools.py: Provides helper functions for vendor selection and response time

Functions:
    run_agent(user_issue: str) -> MaintenanceTask:
        Main agent function to process a user issue and return structured output.

Usage:
    Call `run_agent(user_issue)` with a description of the maintenance issue 
    to receive a validated MaintenanceTask object.
"""

from openai import OpenAI
import json
from schemas import MaintenanceTask
from prompts import MAINTENANCE_PROMPT
from tools import select_vendor, estimate_response_time

client = OpenAI(api_key="YOUR_API_KEY")

def run_agent(user_issue: str) -> MaintenanceTask:
    prompt = MAINTENANCE_PROMPT.format(user_issue=user_issue)
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    
    data = json.loads(response.choices[0].message.content)
    
    # enrich with tools
    data["assigned_vendor"] = select_vendor(data["issue_type"])
    data["estimated_response_time"] = estimate_response_time(data["priority"])
    
    return MaintenanceTask(**data)
