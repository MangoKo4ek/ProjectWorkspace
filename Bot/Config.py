import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
DEBUG = os.getenv("DEBUG")
ADMIN_ID = os.getenv("ADMIN_ID")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
API_HASH = os.getenv("API_HASH")
API_ID = os.getenv("API_ID")
