import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
MODEL_PATH = os.getenv("MODEL_PATH", "/Users/dariprim/Documents/models/YandexGPT-5-Lite-8B-instruct-Q4_K_M.gguf") 
SENTIMENT_MODEL = os.getenv("SENTIMENT_MODEL", "blanchefort/rubert-base-cased-sentiment")