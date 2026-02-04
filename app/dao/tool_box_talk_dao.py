from typing import Optional
from datetime import date

from sqlalchemy import update, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tool_box_talk import ToolBoxTalk


class ToolBoxTalkDAO:
    """站班会数据访问对象"""

    @staticmethod
    async def get_by_id(db: AsyncSession, talk_id: str) -> Optional[ToolBoxTalk]:
        """根据ID查询"""
        stmt = select(ToolBoxTalk).where(
            ToolBoxTalk.id == talk_id,
            ToolBoxTalk.delete_flag == 0
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_ticket_id(db: AsyncSession, ticket_id: str) -> Optional[ToolBoxTalk]:
        """根据作业票ID查询"""
        stmt = select(ToolBoxTalk).where(
            ToolBoxTalk.ticket_id == ticket_id,
            ToolBoxTalk.delete_flag == 0
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def list_all(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[ToolBoxTalk]:
        """查询全部"""
        stmt = (
            select(ToolBoxTalk)
            .where(ToolBoxTalk.delete_flag == 0)
            .order_by(ToolBoxTalk.create_time.desc())
            .offset(skip)
            .limit(limit)
        )
        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def list_by_project(db: AsyncSession, prj_code: str) -> list[ToolBoxTalk]:
        """根据项目编码查询"""
        stmt = select(ToolBoxTalk).where(
            ToolBoxTalk.prj_code == prj_code,
            ToolBoxTalk.delete_flag == 0
        ).order_by(ToolBoxTalk.create_time.desc())
        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def list_by_date(db: AsyncSession, constr_date: date) -> list[ToolBoxTalk]:
        """根据施工日期查询"""
        stmt = select(ToolBoxTalk).where(
            ToolBoxTalk.current_constr_date == constr_date,
            ToolBoxTalk.delete_flag == 0
        ).order_by(ToolBoxTalk.create_time.desc())
        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def list_by_risk_level(db: AsyncSession, risk_level: int) -> list[ToolBoxTalk]:
        """根据风险等级查询"""
        stmt = select(ToolBoxTalk).where(
            ToolBoxTalk.re_assessment_risk_level == risk_level,
            ToolBoxTalk.delete_flag == 0
        ).order_by(ToolBoxTalk.create_time.desc())
        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def insert(db: AsyncSession, entity: ToolBoxTalk) -> ToolBoxTalk:
        """新增"""
        db.add(entity)
        await db.flush()
        return entity

    @staticmethod
    async def update_by_id(db: AsyncSession, talk_id: str, data: dict) -> None:
        """更新"""
        stmt = (
            update(ToolBoxTalk)
            .where(ToolBoxTalk.id == talk_id)
            .values(**data)
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete_by_id(db: AsyncSession, talk_id: str) -> None:
        """删除（物理删除）"""
        stmt = delete(ToolBoxTalk).where(ToolBoxTalk.id == talk_id)
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def soft_delete(db: AsyncSession, talk_id: str) -> None:
        """软删除"""
        stmt = (
            update(ToolBoxTalk)
            .where(ToolBoxTalk.id == talk_id)
            .values(delete_flag=1)
        )
        await db.execute(stmt)
        await db.flush()
