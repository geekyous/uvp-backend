from datetime import datetime

from sqlalchemy import select

import app.core.db as db
from app.models.api_credential import ApiCredential


async def get_secret_by_ak(access_key: str) -> str | None:
    """
    根据 AK 获取 SK
    """
    async with db.AsyncSessionLocal() as session:
        stmt = select(ApiCredential).where(
            ApiCredential.access_key == access_key,
            ApiCredential.status == 1
        )
        result = await session.execute(stmt)
        cred = result.scalar_one_or_none()

        if not cred:
            return None

        if cred.expire_at and cred.expire_at < datetime.utcnow():
            return None

        return cred.secret_key
