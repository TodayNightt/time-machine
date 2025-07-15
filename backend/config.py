import os
from dotenv import load_dotenv

if os.path.exists('.env'):
    load_dotenv()

API_KEY = os.getenv("API_KEY")

ASSETS_DIR = os.getenv("ASSETS_DIR")
