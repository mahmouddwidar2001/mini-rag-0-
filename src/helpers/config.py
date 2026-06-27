from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    DEFAULT_CHUNK_SIZE: int
    
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
