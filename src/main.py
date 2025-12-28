"""
main.py

Purpose:
    Entry point for the Smart Maintenance AI Agent with a simple UI for testing.

Description:
    This module provides a basic Command-Line Interface (CLI) to interact with the AI Agent.
    Users can input a maintenance issue, and the agent returns a structured maintenance plan.

Dependencies:
    - agent.py: Provides the `run_agent` function for processing issues and generating outputs.

Usage:
    Run this script to test the AI Agent interactively via the command line.
    The script will prompt for a maintenance issue and display the resulting MaintenanceTask JSON.
"""

from agent import run_agent

if __name__ == "__main__":
    print("Welcome to Smart Maintenance AI Agent!")
    issue = input("Describe the maintenance issue: ")
    task = run_agent(issue)
    print("\nSuggested Maintenance Plan:")
    print(task.json(indent=4))
