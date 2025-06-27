import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('API_TOKEN')
HEADERS = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json"
    }