import logging
from typing import Optional

from redis.asyncio import Redis

from app.core.config import settings

logger = logging.getLogger(__name__)

_redis: Optional[Redis] = None


async def init_redis():
    """获取redis客户端实例"""
    global _redis
    if _redis is not None:
        return
    _redis = Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
        decode_responses=True,
    )
    await _redis.ping()
    logger.info("Redis connected successfully")


def get_redis() -> Redis:
    """初始化 Redis"""
    if _redis is None:
        raise RuntimeError("Redis client not initialized")
    return _redis


async def close_redis() -> None:
    """关闭 Redis 连接"""
    global _redis
    if _redis:
        await _redis.close()
        _redis = None
        logger.info("Redis client closed")


async def check_redis() -> None:
    """启动阶段 Redis 连接校验"""
    r = get_redis()
    pong = await r.ping()
    if pong is False:
        raise RuntimeError("Redis ping failed")
