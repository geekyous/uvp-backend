from sqlalchemy import text

import app.core.cache as cache
import app.core.db as db

async def check_redis():
    """redis连接检测"""
    if cache.redis_client is None:
        raise RuntimeError("Redis client not initialized")
    try:
        pong = await cache.redis_client.ping()
        if pong is not True:
            raise RuntimeError("redis ping failed")
    except Exception as e:
        raise RuntimeError(f"redis connection failed: {e}")

async def check_mysql():
    """mysql连接检测"""
    try:
        async with db.engine.connect() as conn:
            await conn.execute(text("select 1"))
    except Exception as e:
        raise RuntimeError(f"mysql connection failed: {e}")
