from redis.asyncio import Redis

from app.core.settings import settings

redis_client: Redis | None = None


async def init_redis():
    """初始化 Redis"""
    global redis_client
    if redis_client is None:
        redis_client = Redis.from_url(settings.REDIS_URL, decode_responses=True)


async def close_redis() -> None:
    """关闭 Redis连接"""
    global redis_client
    if redis_client:
        await redis_client.close()
        redis_client = None
