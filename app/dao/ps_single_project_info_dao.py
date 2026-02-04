from typing import Optional

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ps_single_project_info import PsSingleProjectInfo


class PsSingleProjectInfoDAO:
    """单项工程信息数据访问对象"""

    @staticmethod
    async def get_by_id(db: AsyncSession, project_id: str) -> Optional[PsSingleProjectInfo]:
        """根据ID获取单项工程信息"""
        result = await db.execute(
            select(PsSingleProjectInfo).where(PsSingleProjectInfo.id == project_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_safety_code(db: AsyncSession, safety_code: str) -> Optional[PsSingleProjectInfo]:
        """根据安全编码获取项目"""
        result = await db.execute(
            select(PsSingleProjectInfo).where(PsSingleProjectInfo.safety_code == safety_code)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def list_all(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[PsSingleProjectInfo]:
        """获取所有单项工程信息（分页）"""
        result = await db.execute(
            select(PsSingleProjectInfo).offset(skip).limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_by_voltage_level(
        db: AsyncSession, voltage_level: str, skip: int = 0, limit: int = 100
    ) -> list[PsSingleProjectInfo]:
        """根据电压等级获取项目"""
        result = await db.execute(
            select(PsSingleProjectInfo)
            .where(PsSingleProjectInfo.voltage_level == voltage_level)
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_by_build_unit(
        db: AsyncSession, build_unit_code: str, skip: int = 0, limit: int = 100
    ) -> list[PsSingleProjectInfo]:
        """根据建设单位编码获取项目"""
        result = await db.execute(
            select(PsSingleProjectInfo)
            .where(PsSingleProjectInfo.build_unit_code == build_unit_code)
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_by_province(
        db: AsyncSession, province_code: str, skip: int = 0, limit: int = 100
    ) -> list[PsSingleProjectInfo]:
        """根据省份编码获取项目"""
        result = await db.execute(
            select(PsSingleProjectInfo)
            .where(PsSingleProjectInfo.location_province == province_code)
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def insert(db: AsyncSession, entity: PsSingleProjectInfo) -> PsSingleProjectInfo:
        """新增单项工程信息"""
        db.add(entity)
        await db.flush()
        return entity

    @staticmethod
    async def update_by_id(db: AsyncSession, project_id: str, data: dict) -> None:
        """更新单项工程信息"""
        stmt = (
            update(PsSingleProjectInfo)
            .where(PsSingleProjectInfo.id == project_id)
            .values(**data)
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete_by_id(db: AsyncSession, project_id: str) -> None:
        """删除单项工程信息"""
        stmt = delete(PsSingleProjectInfo).where(PsSingleProjectInfo.id == project_id)
        await db.execute(stmt)
        await db.flush()
