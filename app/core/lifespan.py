import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.cache import init_redis, close_redis
from app.core.db import init_mysql, close_mysql
from app.core.health import check_mysql, check_redis

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Application starting...")
    # 初始化 Redis
    await init_redis()
    logger.info("✅ Redis initialized")

    await init_mysql()
    logger.info("✅ MySQL initialized")

    # 校验 Redis
    await check_redis()
    logger.info("✅ Redis connection OK")

    # 校验 MySQL
    await check_mysql()
    logger.info("✅ MySQL connection OK")

    logger.info("🎉 Startup completed")
    yield
    logger.info("🛑 Application shutting down...")

    # 关闭 Redis
    await close_redis()
    logger.info("✅ Redis closed")

    # 关闭 MySQL
    await close_mysql()
    logger.info("✅ MySQL closed")
