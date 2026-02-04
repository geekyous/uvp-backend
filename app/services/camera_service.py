from datetime import datetime
from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.camera_dao import CameraDAO
from app.models.camera import Camera
from app.vo.camera_vo import CameraVO


class CameraService:

    @staticmethod
    async def get(db: AsyncSession, camera_id: str) -> Optional[CameraVO]:
        entity = await CameraDAO.get_by_id(db, camera_id)
        if not entity:
            return None
        return CameraVO.model_validate(entity)

    @staticmethod
    async def list_all(db: AsyncSession) -> List[CameraVO]:
        entities = await CameraDAO.list_all(db)
        return [CameraVO.model_validate(e) for e in entities]

    @staticmethod
    async def create(db: AsyncSession, vo: CameraVO):
        # ⭐ 唯一校验（camera_no + delete_flag）
        exist = await CameraDAO.get_by_camera_no(db, vo.camera_no)
        if exist:
            raise Exception("布控球编码已存在")

        entity = Camera(**vo.model_dump())
        entity.create_time = datetime.now()

        await CameraDAO.insert(db, entity)
        return CameraVO.model_validate(entity)

    @staticmethod
    async def update(db: AsyncSession, camera_id: str, vo: CameraVO):
        data = vo.model_dump(exclude_unset=True)
        data["update_time"] = datetime.now()

        await CameraDAO.update_by_id(db, camera_id, data)
        return await CameraService.get(db, camera_id)

    @staticmethod
    async def delete(db: AsyncSession, camera_id: str):
        """逻辑删除"""
        await CameraDAO.update_by_id(
            db,
            camera_id,
            {
                "delete_flag": 1,
                "update_time": datetime.now()
            }
        )
