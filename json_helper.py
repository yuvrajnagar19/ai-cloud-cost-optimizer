def extract_json(ai_response: str):
    """
    Fallback-safe parser.
    Since AI may not return valid JSON,
    we return a structured default instead.
    """
    return {
        "raw_ai_response": ai_response
    }