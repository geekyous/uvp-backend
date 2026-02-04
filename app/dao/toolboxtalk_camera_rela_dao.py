from typing import Optional

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.camera_rela import ToolBoxTalkCameraRela


class ToolBoxTalkCameraRelaDAO:
    """站班会布控球关联数据访问对象"""

    @staticmethod
    async def get_by_id(db: AsyncSession, rela_id: str) -> Optional[ToolBoxTalkCameraRela]:
        """根据ID查询"""
        stmt = select(ToolBoxTalkCameraRela).where(
            ToolBoxTalkCameraRela.id == rela_id,
            ToolBoxTalkCameraRela.delete_flag == 0
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def list_by_toolbox_id(db: AsyncSession, toolbox_id: str) -> list[ToolBoxTalkCameraRela]:
        """根据站班会ID查询关联的布控球"""
        stmt = select(ToolBoxTalkCameraRela).where(
            ToolBoxTalkCameraRela.tool_box_talk_id == toolbox_id,
            ToolBoxTalkCameraRela.delete_flag == 0
        ).order_by(ToolBoxTalkCameraRela.sort_no)

        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def list_by_camera_id(db: AsyncSession, camera_id: str) -> list[ToolBoxTalkCameraRela]:
        """根据布控球ID查询关联的站班会"""
        stmt = select(ToolBoxTalkCameraRela).where(
            ToolBoxTalkCameraRela.camera_id == camera_id,
            ToolBoxTalkCameraRela.delete_flag == 0
        ).order_by(ToolBoxTalkCameraRela.create_time.desc())

        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def list_all(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[ToolBoxTalkCameraRela]:
        """查询所有关联"""
        stmt = (
            select(ToolBoxTalkCameraRela)
            .where(ToolBoxTalkCameraRela.delete_flag == 0)
            .offset(skip)
            .limit(limit)
        )
        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def insert(db: AsyncSession, entity: ToolBoxTalkCameraRela) -> ToolBoxTalkCameraRela:
        """新增关联"""
        db.add(entity)
        await db.flush()
        return entity

    @staticmethod
    async def update_by_id(db: AsyncSession, rela_id: str, data: dict) -> None:
        """更新关联"""
        stmt = (
            update(ToolBoxTalkCameraRela)
            .where(ToolBoxTalkCameraRela.id == rela_id)
            .values(**data)
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete_by_id(db: AsyncSession, rela_id: str) -> None:
        """删除关联（物理删除）"""
        stmt = delete(ToolBoxTalkCameraRela).where(ToolBoxTalkCameraRela.id == rela_id)
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def soft_delete(db: AsyncSession, rela_id: str) -> None:
        """软删除关联"""
        stmt = (
            update(ToolBoxTalkCameraRela)
            .where(ToolBoxTalkCameraRela.id == rela_id)
            .values(delete_flag=1)
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete_by_toolbox_id(db: AsyncSession, toolbox_id: str) -> None:
        """删除站班会的所有关联（物理删除）"""
        stmt = delete(ToolBoxTalkCameraRela).where(
            ToolBoxTalkCameraRela.tool_box_talk_id == toolbox_id
        )
        await db.execute(stmt)
        await db.flush()
