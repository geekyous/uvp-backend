import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core import cache, database

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Application starting...")
    # 初始化 Redis
    await cache.init_redis()
    logger.info("✅ Redis initialized")

    await database.init_mysql()
    logger.info("✅ MySQL initialized")

    # 校验 Redis
    await cache.check_redis()
    logger.info("✅ Redis connection OK")

    # 校验 MySQL
    await database.check_mysql()
    logger.info("✅ MySQL connection OK")

    logger.info("🎉 Startup completed")

    yield

    logger.info("🛑 Application shutting down...")

    # 关闭 Redis
    await cache.close_redis()
    logger.info("✅ Redis closed")

    # 关闭 MySQL
    await database.close_mysql()
    logger.info("✅ MySQL closed")
