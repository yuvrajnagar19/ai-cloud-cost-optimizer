import json


def analyze_costs():
    """
    Reads project_profile.json and generates cost_report.json
    """

    # Load project profile
    with open("project_profile.json", "r") as f:
        project = json.load(f)

    budget = project.get("budget_inr", 3000)

    # Dummy cost calculation (stable, no AI)
    estimated_cost = 2800

    report = {
        "total_cost": estimated_cost,
        "is_over_budget": estimated_cost > budget,
        "recommendations": [
            "Use smaller EC2 instances",
            "Enable auto-scaling",
            "Use object storage instead of block storage",
            "Monitor costs using AWS Cost Explorer"
        ]
    }

    # Save report
    with open("cost_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("Cost analysis completed. Report saved to cost_report.json")

    return report