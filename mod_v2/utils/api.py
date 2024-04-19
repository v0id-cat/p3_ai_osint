import os

def get_api_key():
    """Retrieve API Key from environment variable."""
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
    return api_key
