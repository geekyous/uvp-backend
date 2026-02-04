from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.device_resource_dao import DeviceResourceDAO
from app.models.device_resource import DeviceResource
from app.vo.device_resource import (DeviceResourceVO)


class DeviceResourceService:

    @staticmethod
    async def get(db: AsyncSession, resource_id: str) -> Optional[DeviceResourceVO]:
        """获取详情"""
        entity = await DeviceResourceDAO.get_by_id(db, resource_id)
        if not entity:
            return None
        return DeviceResourceVO.model_validate(entity)

    @staticmethod
    async def list_children(db: AsyncSession, pid: str, dev_type,
                            protocol_type, status: int) -> List[DeviceResourceVO]:
        """获取子节点列表"""
        entities = await DeviceResourceDAO.list_by_pid(db, pid, dev_type, protocol_type, status)
        return [DeviceResourceVO.model_validate(e) for e in entities]

    @staticmethod
    async def create(db: AsyncSession, vo: DeviceResourceVO):
        """创建资源"""
        entity = DeviceResource(**vo.model_dump())
        await DeviceResourceDAO.insert(db, entity)
        return DeviceResourceVO.model_validate(entity)

    @staticmethod
    async def update(db: AsyncSession, resource_id: str, vo: DeviceResourceVO):
        """更新资源"""
        await DeviceResourceDAO.update_by_id(
            db,
            resource_id,
            vo.model_dump(exclude_unset=True)
        )
        return await DeviceResourceService.get(db, resource_id)

    @staticmethod
    async def delete(db: AsyncSession, resource_id: str):
        """删除资源"""
        await DeviceResourceDAO.delete_by_id(db, resource_id)
