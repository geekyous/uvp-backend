from typing import List

from sqlalchemy import select

from app.core import db
from app.core.mappers.device_resource_mapper import device_resource_to_vo
from app.models.request_respones import QueryResourcesVO
from app.models.resources_model import DeviceResource


async def get_resource(pid, dev_type, protocol_type, status) -> List[QueryResourcesVO]:
    """查询资源"""
    async with db.AsyncSessionLocal() as session:

        stmt = select(DeviceResource)
        if pid:
            stmt = stmt.where(DeviceResource.pid == pid)

        if dev_type:
            stmt = stmt.where(DeviceResource.dev_type.in_(dev_type))

        if status:
            stmt = stmt.where(DeviceResource.status == status)

        stmt = stmt.order_by(DeviceResource.created_time.asc())

        result = await session.execute(stmt)
        resources = result.scalars().all()
        resources_vo = []
        if resources:
            for resource in resources:
                resources_vo.append(device_resource_to_vo(resource))
        return resources_vo
