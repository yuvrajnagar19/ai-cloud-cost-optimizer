import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read API key
API_KEY = os.getenv("HF_API_KEY")

if not API_KEY:
    raise RuntimeError("HF_API_KEY not found. Check your .env file.")

# Hugging Face model endpoint
MODEL_URL = "https://router.huggingface.co/v1/chat/completions"

# Request headers
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
def call_ai(prompt_text, retries=3, wait_seconds=10):
    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [
            {"role": "user", "content": prompt_text}
        ],
        "temperature": 0.3,
        "max_tokens": 300
    }

    for attempt in range(retries):
        response = requests.post(
            MODEL_URL,
            headers=HEADERS,
            json=payload,
            timeout=60
        )

        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]

        elif response.status_code == 503:
            print("Model loading, waiting...")
            time.sleep(wait_seconds)

        else:
            print("Response:", response.text)
            time.sleep(wait_seconds)

    raise RuntimeError("AI service not responding after retries")