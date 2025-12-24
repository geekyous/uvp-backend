import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.cache import init_redis, close_redis
from app.core.db import init_mysql, close_mysql
from app.core.health import check_mysql, check_redis

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Application starting...")
    # 初始化 Redis
    await init_redis()
    print("✅ Redis initialized")

    await init_mysql()
    print("✅ MySQL initialized")

    # 校验 Redis
    await check_redis()
    print("✅ Redis connection OK")

    # 校验 MySQL
    await check_mysql()
    print("✅ MySQL connection OK")

    print("🎉 Startup completed")
    yield
    print("🛑 Application shutting down...")

    # 关闭 Redis
    await close_redis()
    print("✅ Redis closed")

    # 关闭 MySQL
    await close_mysql()
    print("✅ MySQL closed")
