import uuid
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.toolboxtalk_camera_rela_dao import ToolBoxTalkCameraRelaDAO
from app.exceptions.exceptions import BizException
from app.models.camera_rela import ToolBoxTalkCameraRela
from app.vo.toolboxtalk_camera_rela_vo import ToolBoxTalkCameraRelaCreateVO, ToolBoxTalkCameraRelaUpdateVO


class ToolBoxTalkCameraRelaService:

    @staticmethod
    async def create(
            db: AsyncSession,
            vo: ToolBoxTalkCameraRelaCreateVO
    ):
        now = datetime.now()

        entity = ToolBoxTalkCameraRela(
            id=uuid.uuid4().hex,
            camera_id=vo.camera_id,
            tool_box_talk_id=vo.tool_box_talk_id,
            province_code=vo.province_code,
            sort_no=vo.sort_no,
            creater_id=vo.creater_id,
            updater_id=vo.creater_id,
            create_time=now,
            update_time=now,
            delete_flag=0
        )

        await ToolBoxTalkCameraRelaDAO.insert(db, entity)
        await db.commit()
        return entity

    @staticmethod
    async def update(
            db: AsyncSession,
            vo: ToolBoxTalkCameraRelaUpdateVO
    ):
        entity = await ToolBoxTalkCameraRelaDAO.get_by_id(db, vo.id)

        if not entity:
            raise BizException("数据不存在")

        if vo.sort_no is not None:
            entity.sort_no = vo.sort_no

        entity.updater_id = vo.updater_id
        entity.update_time = datetime.now()

        await db.commit()
        return entity

    @staticmethod
    async def delete(
            db: AsyncSession,
            id: str
    ):
        await ToolBoxTalkCameraRelaDAO.soft_delete(db, id)
        await db.commit()

    @staticmethod
    async def list_by_toolbox_id(
            db: AsyncSession,
            toolbox_id: str
    ):
        return await ToolBoxTalkCameraRelaDAO.list_by_toolbox_id(
            db, toolbox_id
        )
