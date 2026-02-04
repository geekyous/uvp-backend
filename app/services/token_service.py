import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.cache import get_redis
from app.core.config import settings
from app.dao.api_credential_dao import ApiCredentialDAO


class TokenService:
    @staticmethod
    async def get_secret_by_ak(db: AsyncSession, access_key: str) -> str | None:
        """
        根据 AK 获取 SK
        """
        return await ApiCredentialDAO.get_secret_by_ak(db, access_key)

    @staticmethod
    async def create_token(ak: str):
        """创建token"""
        token = str(uuid.uuid4())
        await get_redis().setex(f"token:{token}", settings.TOKEN_EXPIRE_SECONDS, ak)
        return token

    @staticmethod
    async def validate_token(token: str):
        ttl = await get_redis().ttl(f"token:{token}")
        if ttl is None or ttl < 0:
            return 0
        return ttl
