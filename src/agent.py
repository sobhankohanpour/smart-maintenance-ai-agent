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
