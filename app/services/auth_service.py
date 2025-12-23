import uuid

import app.core.cache as cache
from app.core.config import settings


def create_token(ak: str) -> str:
    token = str(uuid.uuid4())
    cache.redis_client.setex(
        f"token:{token}",
        settings.TOKEN_EXPIRE_SECONDS,
        ak
    )
    return token


def validate_token(token: str) -> str:
    ttl = cache.redis_client.ttl(f"token:{token}")
    if ttl <= 0:
        return "0"
    return str(ttl)
