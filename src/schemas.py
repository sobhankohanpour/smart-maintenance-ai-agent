"""
schemas.py

Purpose:
    Define structured and validated outputs for the AI Agent using Pydantic.

Description:
    This module contains Pydantic models to ensure that all outputs from the Agent
    are consistent, type-safe, and easy to validate.

Classes:
    MaintenanceTask:
        - issue_type (str): Type of maintenance issue.
        - priority (str): Priority level of the task (e.g., High, Medium, Low).
        - risk (str): Risk assessment associated with the task.
        - recommended_actions (List[str]): List of recommended actions to resolve the issue.
        - assigned_vendor (str): Vendor assigned to handle the task.
        - estimated_response_time (str): Expected response time to address the task.

Usage:
    All AI Agent outputs must conform to the MaintenanceTask model to ensure
    proper validation and structured data handling.
"""

from pydantic import BaseModel
from typing import List

class MaintenanceTask(BaseModel):
    issue_type: str
    priority: str
    risk: str
    recommended_actions: List[str]
    assigned_vendor: str
    estimated_response_time: str
