from logging.config import dictConfig

from app.core.log.filter import RequestIdFilter


def setup_logging():
    dictConfig({
        "version": 1,
        "filters": {
            "request_id": {
                "()": RequestIdFilter
            }
        },
        "formatters": {
            "default": {
                "format": "%(asctime)s %(levelname)s [%(request_id)s] %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "filters": ["request_id"],
                "formatter": "default",
            }
        },
        "root": {
            "handlers": ["console"],
            "level": "INFO"
        }
    })
