from typing import Optional

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.voltage_level import VoltageLevel


class VoltageLevelDAO:
    """电压等级数据访问对象"""

    @staticmethod
    async def get_by_code(db: AsyncSession, level_code: str) -> Optional[VoltageLevel]:
        """根据等级编码获取电压等级"""
        result = await db.execute(
            select(VoltageLevel).where(VoltageLevel.level_code == level_code)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_name(db: AsyncSession, level_name: str) -> Optional[VoltageLevel]:
        """根据等级名称获取电压等级"""
        result = await db.execute(
            select(VoltageLevel).where(VoltageLevel.level_name == level_name)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def list_all(db: AsyncSession) -> list[VoltageLevel]:
        """获取所有电压等级"""
        result = await db.execute(select(VoltageLevel).order_by(VoltageLevel.level_code))
        return list(result.scalars().all())

    @staticmethod
    async def search_by_name(db: AsyncSession, keyword: str) -> list[VoltageLevel]:
        """根据名称关键字搜索电压等级"""
        result = await db.execute(
            select(VoltageLevel)
            .where(VoltageLevel.level_name.like(f"%{keyword}%"))
            .order_by(VoltageLevel.level_code)
        )
        return list(result.scalars().all())

    @staticmethod
    async def insert(db: AsyncSession, entity: VoltageLevel) -> VoltageLevel:
        """新增电压等级"""
        db.add(entity)
        await db.flush()
        return entity

    @staticmethod
    async def update_by_code(db: AsyncSession, level_code: str, data: dict) -> None:
        """更新电压等级"""
        stmt = (
            update(VoltageLevel)
            .where(VoltageLevel.level_code == level_code)
            .values(**data)
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete_by_code(db: AsyncSession, level_code: str) -> None:
        """删除电压等级"""
        stmt = delete(VoltageLevel).where(VoltageLevel.level_code == level_code)
        await db.execute(stmt)
        await db.flush()
