import uuid

from app.core.cache import redis_client
from app.core.config import settings


def create_token(ak: str) -> str:
    token = str(uuid.uuid4())
    redis_client.setex(
        f"token:{token}",
        settings.TOKEN_EXPIRE_SECONDS,
        ak
    )
    return token


def validate_token(token: str) -> str:
    ttl = redis_client.ttl(f"token:{token}")
    if ttl <= 0:
        return "0"
    return str(ttl)
