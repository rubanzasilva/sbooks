
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL:str
    JWT_SECRET:str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

