from typing import Optional
from datetime import datetime, date

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.construction_work_ticket import ConstructionWorkTicket


class ConstructionWorkTicketDAO:
    """施工作业票数据访问对象"""

    @staticmethod
    async def get_by_id(db: AsyncSession, ticket_id: str) -> Optional[ConstructionWorkTicket]:
        """根据ID获取施工作业票"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.id == ticket_id,
                ConstructionWorkTicket.delete_flag == 0
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_ticket_no(db: AsyncSession, ticket_no: str) -> Optional[ConstructionWorkTicket]:
        """根据作业票编号获取"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.ticket_no == ticket_no,
                ConstructionWorkTicket.delete_flag == 0
            )
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_single_project(
        db: AsyncSession, single_project_code: str
    ) -> list[ConstructionWorkTicket]:
        """根据单项工程编码获取作业票列表"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.single_project_code == single_project_code,
                ConstructionWorkTicket.delete_flag == 0
            ).order_by(ConstructionWorkTicket.create_time.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_all(
        db: AsyncSession, skip: int = 0, limit: int = 100
    ) -> list[ConstructionWorkTicket]:
        """查询所有施工作业票（分页）"""
        result = await db.execute(
            select(ConstructionWorkTicket)
            .where(ConstructionWorkTicket.delete_flag == 0)
            .order_by(ConstructionWorkTicket.create_time.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_by_team_id(
        db: AsyncSession, team_id: str
    ) -> list[ConstructionWorkTicket]:
        """根据班组ID获取作业票列表"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.team_id == team_id,
                ConstructionWorkTicket.delete_flag == 0
            ).order_by(ConstructionWorkTicket.create_time.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_by_status(
        db: AsyncSession, ticket_status: str
    ) -> list[ConstructionWorkTicket]:
        """根据作业票状态获取列表"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.ticket_status == ticket_status,
                ConstructionWorkTicket.delete_flag == 0
            ).order_by(ConstructionWorkTicket.create_time.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_by_bidding_section(
        db: AsyncSession, bidding_section_code: str
    ) -> list[ConstructionWorkTicket]:
        """根据标段编码获取作业票列表"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.bidding_section_code == bidding_section_code,
                ConstructionWorkTicket.delete_flag == 0
            ).order_by(ConstructionWorkTicket.create_time.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_by_date_range(
        db: AsyncSession, start_date: date, end_date: date
    ) -> list[ConstructionWorkTicket]:
        """根据日期范围获取作业票"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.start_time >= start_date,
                ConstructionWorkTicket.end_time <= end_date,
                ConstructionWorkTicket.delete_flag == 0
            ).order_by(ConstructionWorkTicket.create_time.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_by_risk_level(
        db: AsyncSession, risk_level: int
    ) -> list[ConstructionWorkTicket]:
        """根据风险等级获取作业票"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.re_assessment_risk_level == risk_level,
                ConstructionWorkTicket.delete_flag == 0
            ).order_by(ConstructionWorkTicket.create_time.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_by_build_unit(
        db: AsyncSession, build_unit_code: str
    ) -> list[ConstructionWorkTicket]:
        """根据建设单位编码获取作业票"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.build_unit_code == build_unit_code,
                ConstructionWorkTicket.delete_flag == 0
            ).order_by(ConstructionWorkTicket.create_time.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_by_construction_status(
        db: AsyncSession, construction_status: str
    ) -> list[ConstructionWorkTicket]:
        """根据施工状态获取作业票"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.current_construction_status == construction_status,
                ConstructionWorkTicket.delete_flag == 0
            ).order_by(ConstructionWorkTicket.create_time.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_active(
        db: AsyncSession, skip: int = 0, limit: int = 100
    ) -> list[ConstructionWorkTicket]:
        """查询正在执行的作业票（状态为05-执行中）"""
        result = await db.execute(
            select(ConstructionWorkTicket).where(
                ConstructionWorkTicket.ticket_status == "05",
                ConstructionWorkTicket.delete_flag == 0
            ).order_by(ConstructionWorkTicket.create_time.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def insert(db: AsyncSession, entity: ConstructionWorkTicket) -> ConstructionWorkTicket:
        """新增施工作业票"""
        db.add(entity)
        await db.flush()
        return entity

    @staticmethod
    async def update_by_id(
        db: AsyncSession, ticket_id: str, data: dict
    ) -> None:
        """更新施工作业票"""
        stmt = (
            update(ConstructionWorkTicket)
            .where(ConstructionWorkTicket.id == ticket_id)
            .values(**data)
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete_by_id(db: AsyncSession, ticket_id: str) -> None:
        """删除施工作业票（物理删除）"""
        stmt = delete(ConstructionWorkTicket).where(
            ConstructionWorkTicket.id == ticket_id
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def soft_delete(db: AsyncSession, ticket_id: str) -> None:
        """软删除施工作业票"""
        stmt = (
            update(ConstructionWorkTicket)
            .where(ConstructionWorkTicket.id == ticket_id)
            .values(delete_flag=1)
        )
        await db.execute(stmt)
        await db.flush()
