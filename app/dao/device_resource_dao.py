from typing import Optional

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.device_resource import DeviceResource


class DeviceResourceDAO:
    """设备资源数据访问对象"""

    @staticmethod
    async def get_by_id(db: AsyncSession, resource_id: str) -> Optional[DeviceResource]:
        """根据ID查询"""
        stmt = select(DeviceResource).where(DeviceResource.id == resource_id)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_dev_code(db: AsyncSession, dev_code: str) -> Optional[DeviceResource]:
        """根据设备编码查询"""
        stmt = select(DeviceResource).where(DeviceResource.dev_code == dev_code)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    @staticmethod
    async def list_by_pid(
            db: AsyncSession,
            pid: str = None,
            dev_type: list[str] = None,
            protocol_type: str = None,
            status: int = None
    ) -> list[DeviceResource]:
        """查询子节点"""
        stmt = select(DeviceResource)

        if pid:
            stmt = stmt.where(DeviceResource.pid == pid)
        if dev_type:
            stmt = stmt.where(DeviceResource.dev_type.in_(dev_type))
        if status is not None:
            stmt = stmt.where(DeviceResource.status == status)

        stmt = stmt.order_by(DeviceResource.order)
        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def list_by_type(db: AsyncSession, dev_type: str) -> list[DeviceResource]:
        """根据设备类型查询"""
        stmt = select(DeviceResource).where(DeviceResource.dev_type == dev_type)
        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def list_all(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[DeviceResource]:
        """查询全部"""
        stmt = select(DeviceResource).offset(skip).limit(limit)
        result = await db.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def insert(db: AsyncSession, entity: DeviceResource) -> DeviceResource:
        """新增"""
        db.add(entity)
        await db.flush()
        return entity

    @staticmethod
    async def update_by_id(db: AsyncSession, resource_id: str, data: dict) -> None:
        """更新"""
        stmt = (
            update(DeviceResource)
            .where(DeviceResource.id == resource_id)
            .values(**data)
        )
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete_by_id(db: AsyncSession, resource_id: str) -> None:
        """删除"""
        stmt = delete(DeviceResource).where(DeviceResource.id == resource_id)
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def update_children_count(db: AsyncSession, pid: str) -> None:
        """更新子节点数量"""
        # 查询子节点数量
        count_stmt = select(DeviceResource).where(DeviceResource.pid == pid)
        result = await db.execute(count_stmt)
        count = len(list(result.scalars().all()))

        # 更新父节点的children_count和has_children
        update_stmt = (
            update(DeviceResource)
            .where(DeviceResource.id == pid)
            .values(children_count=count, has_children=(count > 0))
        )
        await db.execute(update_stmt)
        await db.flush()
