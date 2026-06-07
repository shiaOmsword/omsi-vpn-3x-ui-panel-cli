import os
from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator


BASE_DIR = Path(__file__).resolve().parents[3]
ENVIRONMENT = os.getenv("APP_ENV", "local")
ENV_FILE = BASE_DIR / ".envs" / f".{ENVIRONMENT}.env"

class Settings(BaseSettings):
    environment: str = Field(default=ENVIRONMENT, alias="APP_ENV")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    panel_token: str = "panel_token"
    logs_dir: Path = BASE_DIR / "data" / "logs"
    base_url:str = "https://url.com"
    base_url_sub:str = "https://sub.com"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True,
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()