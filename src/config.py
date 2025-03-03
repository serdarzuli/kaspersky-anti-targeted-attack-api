import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

BASE_URL = "https://10.10.101.200:443/kata/scanner/v1"
CLIENT_CERT = os.getenv("CLIENT_CERT")
CLIENT_KEY = os.getenv("CLIENT_KEY")
TOKEN = os.getenv("API_TOKEN")
