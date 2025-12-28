from pydantic import BaseModel
from typing import List

class MaintenanceTask(BaseModel):
    issue_type: str
    priority: str
    risk: str
    recommended_actions: List[str]
    assigned_vendor: str
    estimated_response_time: str
