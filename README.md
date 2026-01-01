# AI Cloud Cost Optimizer

A simple Python CLI tool that uses AI (Hugging Face LLM) to estimate cloud costs and provide optimization suggestions based on your project description.

## Features
- Input your project description via command line
- AI generates a realistic (fake) monthly billing breakdown
- Automatic cost analysis with budget comparison
- Practical optimization recommendations
- View a clean summary of results

## Project Files
- `main_cli.py` – Main program with menu
- `project_input.txt` – Stores your project description
- `project_profile.json` – Auto-generated project profile
- `billing_data.json` – Auto-generated sample billing data
- `cost_report.json` – Final cost report and recommendations
- `ai_client.py` – Handles API calls to Hugging Face
- `json_helper.py` – Safely parses AI responses
- `project_profile.py` – Generates project profile from description
- `billing_engine.py` – Creates fake billing data using AI
- `cost_engine.py` – Analyzes costs and generates report
- `summary_view.py` – Displays summary of results

## Requirements
- Python 3.7+
- Internet connection (for Hugging Face API)

## Setup

1. Clone or download this project folder.

2. Install required packages:
   ```bash
   pip install requests python-dotenv