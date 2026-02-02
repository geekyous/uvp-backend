import logging
from typing import Optional

from sqlalchemy import engine, text
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.core.config import settings

logger = logging.getLogger(__name__)

_db_url = engine.url.URL.create(
    drivername="mysql+aiomysql",
    username=settings.MYSQL_USER,
    password=settings.MYSQL_PASSWORD,
    host=settings.MYSQL_HOST,
    port=settings.MYSQL_PORT,
    database=settings.MYSQL_DATABASE,
)

_engine = None
_SessionFactory: Optional[async_sessionmaker[AsyncSession]] = None


async def init_mysql():
    global _engine, _SessionFactory

    if _engine:
        return

    _engine = create_async_engine(
        _db_url,
        pool_pre_ping=True,
        pool_recycle=3600,
        echo=True,
    )

    _SessionFactory = async_sessionmaker(
        bind=_engine,
        expire_on_commit=False,
        autoflush=False,
    )

    # 启动即校验
    async with _engine.connect() as conn:
        await conn.execute(text("SELECT 1"))

    logger.info("MySQL connected successfully")


def get_db() -> AsyncSession:
    if _SessionFactory is None:
        raise RuntimeError("Database not initialized")
    return _SessionFactory()


async def check_mysql():
    async with _engine.connect() as conn:
        await conn.execute(text("SELECT 1"))


async def close_mysql():
    global _engine
    if _engine:
        await _engine.dispose()
        _engine = None
        logger.info("MySQL connection closed")
