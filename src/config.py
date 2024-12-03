import os
from dotenv import load_dotenv

load_dotenv()

def get_google_api_key():
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise EnvironmentError("GOOGLE_API_KEY environment variable not set. Please set it to your Google Generative AI API key.")
    return api_key