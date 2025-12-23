from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine

from app.core.config import settings

engine: AsyncEngine | None = None
AsyncSessionLocal = None


async def init_mysql() -> None:
    """初始化 MySQL"""
    global engine, AsyncSessionLocal
    if engine is None:
        engine = create_async_engine(
            settings.MYSQL_URL,
            pool_pre_ping=True,
            pool_size=5,
            max_overflow=10,
        )
        AsyncSessionLocal = async_sessionmaker(
            engine,
            expire_on_commit=False,
        )


async def close_mysql() -> None:
    """关闭 MySQL"""
    global engine
    if engine:
        await engine.dispose()
        engine = None
