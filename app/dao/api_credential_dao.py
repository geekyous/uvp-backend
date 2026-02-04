from datetime import datetime
from typing import Optional

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.api_credential import ApiCredential


class ApiCredentialDAO:
    """API凭证数据访问对象"""

    @staticmethod
    async def get_by_ak(db: AsyncSession, access_key: str) -> Optional[ApiCredential]:
        """根据AK获取凭证"""
        result = await db.execute(
            select(ApiCredential).where(ApiCredential.access_key == access_key)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_secret_by_ak(db: AsyncSession, access_key: str) -> str | None:
        """根据 AK 获取 SK（验证状态和过期时间）"""
        result = await db.execute(
            select(ApiCredential).where(
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

    @staticmethod
    async def list_all(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[ApiCredential]:
        """获取所有凭证"""
        result = await db.execute(
            select(ApiCredential).offset(skip).limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_active(db: AsyncSession) -> list[ApiCredential]:
        """获取所有有效凭证"""
        result = await db.execute(
            select(ApiCredential).where(
                ApiCredential.status == 1,
                ApiCredential.expire_at > datetime.utcnow()
            )
        )
        return list(result.scalars().all())

    @staticmethod
    async def insert(db: AsyncSession, entity: ApiCredential) -> ApiCredential:
        """新增凭证"""
        db.add(entity)
        await db.flush()
        return entity

    @staticmethod
    async def update_by_ak(db: AsyncSession, access_key: str, data: dict) -> None:
        """更新凭证"""
        stmt = (
            update(ApiCredential)
            .where(ApiCredential.access_key == access_key)
            .values(**data)
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete_by_ak(db: AsyncSession, access_key: str) -> None:
        """删除凭证"""
        stmt = delete(ApiCredential).where(ApiCredential.access_key == access_key)
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def deactivate(db: AsyncSession, access_key: str) -> None:
        """禁用凭证"""
        stmt = (
            update(ApiCredential)
            .where(ApiCredential.access_key == access_key)
            .values(status=0)
        )
        await db.execute(stmt)
        await db.flush()
