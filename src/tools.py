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
