"""
prompts.py

Purpose:
    Define prompt templates for Large Language Models (LLMs) used by the AI Agent.

Description:
    This module contains the main prompt and reusable templates to ensure
    clarity, consistency, and maintainability when interacting with the AI Agent.

Constants:
    MAINTENANCE_PROMPT (str): Main prompt template instructing the agent to:
        1. Identify the issue type
        2. Assign priority (Low, Medium, High)
        3. Assess risk
        4. Suggest recommended actions
        5. Assign an appropriate vendor
        6. Estimate response time
        The output should be returned as JSON conforming to the MaintenanceTask schema.

Usage:
    Use these prompt templates when sending user issues to the AI Agent for processing.
"""

MAINTENANCE_PROMPT = """
You are a smart maintenance AI agent. 
User describes an issue. 
Your tasks:
1. Identify issue_type
2. Assign priority (Low, Medium, High)
3. Assess risk
4. Suggest recommended actions
5. Assign appropriate vendor
6. Estimate response time

Return the output as JSON matching the MaintenanceTask schema.
User issue: {user_issue}
"""
