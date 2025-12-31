import json
from ai_client import call_ai
from json_helper import extract_json

def generate_billing(project_profile):
    prompt = f"""
Create realistic cloud billing data in STRICT JSON array format.

Project details:
{project_profile}

Each record must include:
service
usage
cost_inr
description

Return ONLY JSON array.
"""

    ai_response = call_ai(prompt)
    billing = extract_json(ai_response)

    with open("billing_data.json", "w") as f:
        json.dump(billing, f, indent=2)

    return billing