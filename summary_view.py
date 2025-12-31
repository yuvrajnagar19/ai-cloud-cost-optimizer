import json
import os

def show_summary():
    if not os.path.exists("cost_report.json"):
        print("⚠️ No cost report found. Please run cost analysis first.")
        return

    with open("cost_report.json") as f:
        report = json.load(f)

    print("\n===== COST OPTIMIZATION SUMMARY =====")
    print("Total Cost:", report["total_cost"])
    print("Over Budget:", report["is_over_budget"])
    print("\nRecommendations:")
    for i, rec in enumerate(report["recommendations"], start=1):
        print(f"{i}. {rec}")