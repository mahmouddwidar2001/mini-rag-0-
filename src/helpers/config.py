from pydantic_settings  import BaseSettings 

class settings(BaseSettings):
    APP_NAME : str 
    APP_VERSION : str
    openai_api_key : str


    class Config:
        env_file = ".env"

def get_settings():
    return settings()