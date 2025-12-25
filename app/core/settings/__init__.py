import os

from app.core.settings.dev import DevSettings
from app.core.settings.prod import ProdSettings
from app.core.settings.test import TestSettings


def load_settings():
    env = os.getenv("APP_ENV", "dev")

    if env == "prod":
        return ProdSettings()
    if env == "test":
        return TestSettings()
    return DevSettings()

settings = load_settings()
