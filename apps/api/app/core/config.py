from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BASE_DIR / ".env"


class Settings(BaseSettings):
    app_name: str = "QEVYRA AI"
    app_version: str = "0.1.0"
    environment: str = "development"
    debug: bool = True

    api_host: str = "0.0.0.0"
    api_port: int = 8002

    database_url: str
    redis_url: str

    jwt_secret: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    openai_api_key: str = ""
    openai_base_url: str = "https://api.openai.com/v1"

    apynex_api_key: str = ""
    apynex_base_url: str = "https://api.apinex.bond/v1"

    xkiro_api_key: str = ""
    xkiro_base_url: str = ""

    unorouter_api_key: str = ""
    unorouter_base_url: str = "https://api.unorouter.com/v1"

    google_api_key: str = ""

    default_model: str = ""

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
