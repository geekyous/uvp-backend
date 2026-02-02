from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.api_credential import ApiCredential


class ApiCredentialDao:

    @staticmethod
    async def get_secret_by_ak(db: AsyncSession, access_key: str) -> str | None:
        """
        根据 AK 获取 SK
        """
        result = await db.execute(select(ApiCredential)
        .where(
            ApiCredential.access_key == access_key,
            ApiCredential.status == 1
        )
        )
        cred = result.scalar_one_or_none()
        if cred is None:
            return None
        if cred.expire_at and cred.expire_at < datetime.utcnow():
            return None
        return cred.secret_key
