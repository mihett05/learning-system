import os
from functools import lru_cache
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Config:
    CHAT_ID: int = os.getenv("CHAT_ID")
    API_TOKEN: str = os.getenv("API_TOKEN")
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL")
    PROJECT_PATH = Path(__file__).resolve().parent
    DB = PROJECT_PATH / "database.json"


@lru_cache
def get_config() -> Config:
    return Config()
