from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="UVP",  # 可选：环境变量前缀
        case_sensitive=False
    )

    # 环境变量名：MYSQL_URL
    mysql_url: str = "mysql+pymysql://root:root@127.0.0.1:3306/uvp"

    # 环境变量名：REDIS_URL
    redis_url: str = "redis://:root@127.0.0.1:6379/1"

    # 环境变量名：TOKEN_EXPIRE_SECONDS
    token_expire_seconds: int = 1800

    # 环境变量名：NONCE_TTL_SECONDS
    nonce_ttl_seconds: int = 300


settings = Settings()
