from pydantic_settings import SettingsConfigDict

from app.core.settings.base import BaseAppSettings


class ProdSettings(BaseAppSettings):
    model_config = SettingsConfigDict(
        env_file=None  # 生产环境不读 .env
    )
