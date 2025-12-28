"""
tools.py

Purpose:
    Provide small helper functions that the AI Agent can call during task processing.

Description:
    This module contains utility functions for common operations such as
    vendor selection, response time estimation, and task prioritization.
    These functions help standardize agent behavior and simplify code reuse.

Functions:
    select_vendor(issue_type: str) -> str:
        Returns the appropriate vendor for a given issue type.
        Defaults to "General Maintenance Team" if issue type is unknown.

    estimate_response_time(priority: str) -> str:
        Returns the estimated response time based on task priority.
        Defaults to "24 hours" if priority is unknown.

Usage:
    Import these functions in the agent workflow to handle task-specific operations.
"""

def select_vendor(issue_type: str) -> str:
    vendors = {
        "HVAC": "HVAC Team A",
        "Plumbing": "Plumber Team B",
        "Electrical": "Electrician Team C"
    }
    return vendors.get(issue_type, "General Maintenance Team")

def estimate_response_time(priority: str) -> str:
    mapping = {"High": "2 hours", "Medium": "6 hours", "Low": "24 hours"}
    return mapping.get(priority, "24 hours")
