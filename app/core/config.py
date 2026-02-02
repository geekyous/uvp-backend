from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "UAP Backend Service"
    ENV: str = "dev"
    DEBUG: bool = False

    # ===== Database =====
    MYSQL_HOST: str = None
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = None
    MYSQL_PASSWORD: str = None
    MYSQL_DATABASE: str = None
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DB_POOL_TIMEOUT: int = 30
    DB_POOL_RECYCLE: int = 1800

    # ===== Redis =====
    REDIS_HOST: str = "127.0.0.1"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str | None = None
    REDIS_MAX_CONNECTIONS: int = 50
    REDIS_SOCKET_TIMEOUT: int = 5

    # ===== Logging =====
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"

    TOKEN_EXPIRE_SECONDS: int = 1800
    NONCE_TTL_SECONDS: int = 600

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


settings = Settings()
