import json
from ai_client import call_ai
from json_helper import extract_json

def generate_project_profile(description):
    prompt = f"""
Convert the following project description into STRICT JSON.

Required fields:
project_name
monthly_budget
tech_stack
description

Project description:
{description}

Return ONLY JSON.
"""

    def generate_project_profile(description: str):
        return {
            "description": description,
            "estimated_services": [
                "Compute (EC2 / VM)",
                "Storage",
                "Networking",
                "Managed Database"
            ]
        }

    with open("project_profile.json", "w") as f:
        json.dump(profile, f, indent=2)

    return profile