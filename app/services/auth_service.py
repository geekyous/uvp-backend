import uuid

import app.core.cache as cache
from app.core.settings import settings


async def create_token(ak: str) -> str:
    token = str(uuid.uuid4())
    await cache.redis_client.setex(
        f"token:{token}",
        settings.TOKEN_EXPIRE_SECONDS,
        ak
    )
    return token


async def validate_token(token: str):
    ttl = await cache.redis_client.ttl(f"token:{token}")
    print(ttl)
    if ttl is None or ttl <= 0:
        return 0
    return ttl
