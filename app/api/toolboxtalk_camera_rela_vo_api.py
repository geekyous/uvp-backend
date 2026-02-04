from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.response import ApiResponse, success
from app.core.security import auth_dependency
from app.dao.toolboxtalk_camera_rela_dao import ToolBoxTalkCameraRelaDAO
from app.vo.toolboxtalk_camera_rela_vo import ToolBoxTalkCameraRelaCreateVO

router = APIRouter(prefix="/uvp-backend-common/api/v1/tool-box-talk-camera-rela", tags=["站班会布控球关联"],
                   dependencies=[Depends(auth_dependency)], )


@router.post("", summary="添加站班会布控球关联数据数据",
             description="添加站班会布控球关键数据", response_model=ApiResponse)
async def create(create_vo: ToolBoxTalkCameraRelaCreateVO, db: AsyncSession = Depends(get_db)):
    await ToolBoxTalkCameraRelaDAO.insert(db, create_vo)
    return success()


@router.get("", summary="添加站班会布控球关键数据",
            description="添加站班会布控球关键数据", response_model=ApiResponse)
async def query(tool_box_id: str, db: AsyncSession = Depends(get_db)):
    tool_box_camera_rela_list = ToolBoxTalkCameraRelaDAO.list_by_toolbox_id(db, tool_box_id)
    return success(tool_box_camera_rela_list)
