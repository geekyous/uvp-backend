from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.response import ApiResponse, success
from app.core.security import auth_dependency
from app.services.camera_service import CameraService
from app.vo.camera_vo import CameraVO

router = APIRouter(prefix="/uvp-backend-common/api/v1/camera", tags=["布控球数据"],
                   dependencies=[Depends(auth_dependency)], )


@router.post("", summary="添加布控球数据",
             description="添加布控球数据", response_model=ApiResponse)
async def create(camera_vo: CameraVO, db: AsyncSession = Depends(get_db), ):
    camera = await CameraService.create(db, camera_vo)
    return success(camera)


@router.post("/query", summary="查询布控球数据",
             description="查询布控球数据")
async def query(db: AsyncSession = Depends(get_db), ):
    cameras = CameraService.list_all(db)
    return success(cameras)
