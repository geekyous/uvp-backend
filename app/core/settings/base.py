from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseAppSettings(BaseSettings):
    APP_NAME: str = "uvp-backend"
    APP_ENV: str = Field(..., description="dev / test/ prod")

    MYSQL_URL: str
    REDIS_URL: str

    TOKEN_EXPIRE_SECONDS: int = 1800
    NONCE_TTL_SECONDS: int = 600

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="forbid",
    )
