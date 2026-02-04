from typing import Optional

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.device_type import DeviceType


class DeviceTypeDAO:
    """设备类型数据访问对象"""

    @staticmethod
    async def get_by_code(db: AsyncSession, type_code: str) -> Optional[DeviceType]:
        """根据类型编码获取设备类型"""
        result = await db.execute(
            select(DeviceType).where(DeviceType.type_code == type_code)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_name(db: AsyncSession, type_name: str) -> Optional[DeviceType]:
        """根据类型名称获取设备类型"""
        result = await db.execute(
            select(DeviceType).where(DeviceType.type_name == type_name)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def list_all(db: AsyncSession) -> list[DeviceType]:
        """获取所有设备类型"""
        result = await db.execute(select(DeviceType).order_by(DeviceType.type_code))
        return list(result.scalars().all())

    @staticmethod
    async def search_by_name(db: AsyncSession, keyword: str) -> list[DeviceType]:
        """根据名称关键字搜索设备类型"""
        result = await db.execute(
            select(DeviceType)
            .where(DeviceType.type_name.like(f"%{keyword}%"))
            .order_by(DeviceType.type_code)
        )
        return list(result.scalars().all())

    @staticmethod
    async def insert(db: AsyncSession, entity: DeviceType) -> DeviceType:
        """新增设备类型"""
        db.add(entity)
        await db.flush()
        return entity

    @staticmethod
    async def update_by_code(db: AsyncSession, type_code: str, data: dict) -> None:
        """更新设备类型"""
        stmt = (
            update(DeviceType)
            .where(DeviceType.type_code == type_code)
            .values(**data)
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete_by_code(db: AsyncSession, type_code: str) -> None:
        """删除设备类型"""
        stmt = delete(DeviceType).where(DeviceType.type_code == type_code)
        await db.execute(stmt)
        await db.flush()
