from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )

    # 环境变量名：MYSQL_URL
    MYSQL_URL: str = "mysql+pymysql://root:root@127.0.0.1:3306/uvp"

    # 环境变量名：REDIS_URL
    REDIS_URL: str = "redis://:root@127.0.0.1:6379/1"

    # 环境变量名：TOKEN_EXPIRE_SECONDS
    TOKEN_EXPIRE_SECONDS: int = 1800

    # 环境变量名：NONCE_TTL_SECONDS
    NONCE_TTL_SECONDS: int = 300


settings = Settings()
