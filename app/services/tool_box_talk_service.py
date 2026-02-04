from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.tool_box_talk_dao import ToolBoxTalkDAO
from app.models.tool_box_talk import ToolBoxTalk
from app.vo.tool_box_talk import ToolBoxTalkVO


class DeviceResourceService:

    @staticmethod
    async def get(db: AsyncSession, resource_id: str) -> Optional[ToolBoxTalkVO]:
        """获取详情"""
        entity = await ToolBoxTalkDAO.get_by_id(db, resource_id)
        if not entity:
            return None
        return ToolBoxTalkVO.model_validate(entity)

    @staticmethod
    async def create(db: AsyncSession, vo: ToolBoxTalkVO):
        """创建资源"""
        entity = ToolBoxTalk(**vo.model_dump())
        await ToolBoxTalkDAO.insert(db, entity)
        return ToolBoxTalkVO.model_validate(entity)

    @staticmethod
    async def update(db: AsyncSession, resource_id: str, vo: ToolBoxTalkVO):
        """更新资源"""
        await ToolBoxTalkDAO.update_by_id(
            db,
            resource_id,
            vo.model_dump(exclude_unset=True)
        )
        return await DeviceResourceService.get(db, resource_id)

    @staticmethod
    async def delete(db: AsyncSession, resource_id: str):
        """删除资源"""
        await ToolBoxTalkDAO.delete_by_id(db, resource_id)
