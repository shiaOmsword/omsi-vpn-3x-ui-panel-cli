import os
import sys
from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def get_runtime_base_dir() -> Path:
    """
    Папка приложения:
    - для exe: папка, где лежит panel-launcher.exe
    - для обычного запуска: корень проекта
    """
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    return Path(__file__).resolve().parents[3]


BASE_DIR = get_runtime_base_dir()
ENVIRONMENT = os.getenv("APP_ENV", "local")
ENV_FILE = BASE_DIR / ".envs" / f".{ENVIRONMENT}.env"


class Settings(BaseSettings):
    environment: str = Field(default=ENVIRONMENT, alias="APP_ENV")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    panel_token: str = Field(alias="PANEL_TOKEN")
    base_url: str = Field(alias="BASE_URL")
    base_url_sub: str = Field(alias="BASE_URL_SUB")

    logs_dir: Path = BASE_DIR / "data" / "logs"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
        populate_by_name=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()