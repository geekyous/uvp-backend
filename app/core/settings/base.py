from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseAppSettings(BaseSettings):
    APP_NAME: str = "uvp-backend"
    APP_ENV: str = Field(..., description="dev / test/ prod")

    MYSQL_HOST: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_PORT: int
    MYSQL_DATABASE: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str
    REDIS_DB: int

    TOKEN_EXPIRE_SECONDS: int = 1800
    NONCE_TTL_SECONDS: int = 600

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="forbid",
    )
