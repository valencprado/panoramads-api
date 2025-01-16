from functools import lru_cache
from pydantic_settings import BaseSettings
import os


class AppSettings(BaseSettings):
    app_name: str = "PanoramADS API"
    project_id: str
    private_key_id: str
    private_key: str
    client_email: str
    client_id: str
    client_url: str
    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> AppSettings:
    settings = AppSettings()
    return settings
