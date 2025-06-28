import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('API_TOKEN')
if not TOKEN:
    raise ValueError("[ERROR] TOKEN is not set in .env")

HEADERS = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json"
    }

ORG_NAME = os.getenv("ORG_NAME")
if not ORG_NAME:
    raise ValueError("[ERROR] ORG_NAME is not set in .env")