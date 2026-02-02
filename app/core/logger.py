import logging
import os
from logging.handlers import RotatingFileHandler

from app.core.config import settings


def setup_logging():
    os.makedirs("logs", exist_ok=True)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    )

    file_handler = RotatingFileHandler(
        settings.LOG_FILE,
        maxBytes=50 * 1024 * 1024,
        backupCount=10,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        handlers=[file_handler, console_handler],
    )
