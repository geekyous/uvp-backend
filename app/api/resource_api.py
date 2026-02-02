from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.response import success, ApiResponse
from app.core.security import auth_dependency

router = APIRouter(prefix="/uvp-backend-common/api/v1", tags=["资源服务"],
                   dependencies=[Depends(auth_dependency)], )


@router.post("/resource/queryResources", summary="逐层查询资源树信息",
             description="逐层获取资源树资源信息", response_model=ApiResponse)
async def query_resources(db: AsyncSession = Depends(get_db)):
    return success()


@router.post("/resource/mock", summary="生成资源仿真数据",
             description="逐层获取资源树资源信息", response_model=ApiResponse)
async def mock_resource():
    return success()
