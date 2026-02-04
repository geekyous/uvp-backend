from typing import Optional

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.camera import Camera


class CameraDAO:
    """布控球数据访问对象"""

    @staticmethod
    async def get_by_id(db: AsyncSession, camera_id: str) -> Optional[Camera]:
        """根据ID查询布控球"""
        stmt = select(Camera).where(
            Camera.id == camera_id,
            Camera.delete_flag == 0
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_camera_no(db: AsyncSession, camera_no: str) -> Optional[Camera]:
        """根据布控球编码查询"""
        stmt = select(Camera).where(
            Camera.camera_no == camera_no,
            Camera.delete_flag == 0
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def list_all(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Camera]:
        """查询布控球列表"""
        stmt = (
            select(Camera)
            .where(Camera.delete_flag == 0)
            .offset(skip)
            .limit(limit)
        )
        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def list_by_province(db: AsyncSession, province_code: str) -> list[Camera]:
        """根据省份编码查询布控球列表"""
        stmt = select(Camera).where(
            Camera.province_code == province_code,
            Camera.delete_flag == 0
        )
        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def insert(db: AsyncSession, entity: Camera) -> Camera:
        """新增布控球"""
        db.add(entity)
        await db.flush()
        return entity

    @staticmethod
    async def update_by_id(db: AsyncSession, camera_id: str, data: dict) -> None:
        """根据ID更新布控球"""
        stmt = (
            update(Camera)
            .where(Camera.id == camera_id)
            .values(**data)
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete_by_id(db: AsyncSession, camera_id: str) -> None:
        """根据ID删除布控球（物理删除）"""
        stmt = delete(Camera).where(Camera.id == camera_id)
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def soft_delete(db: AsyncSession, camera_id: str) -> None:
        """软删除布控球"""
        stmt = (
            update(Camera)
            .where(Camera.id == camera_id)
            .values(delete_flag=1)
        )
        await db.execute(stmt)
        await db.flush()
