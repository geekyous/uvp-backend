from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.response import success, ApiResponse
from app.core.security import auth_dependency
from app.services.device_resource_service import DeviceResourceService
from app.vo.device_resource import QueryResource

router = APIRouter(prefix="/uvp-backend-common/api/v1", tags=["资源服务"],
                   dependencies=[Depends(auth_dependency)], )


@router.post("/resource/queryResources", summary="逐层查询资源树信息",
             description="逐层获取资源树资源信息", response_model=ApiResponse)
async def query_resources(req: QueryResource, db: AsyncSession = Depends(get_db)):
    pid = req.pid
    dev_type = req.devType
    status = req.status
    protocol_type = req.protocolType
    resources = await DeviceResourceService.list_children(db, pid=pid, dev_type=dev_type,
                                                          protocol_type=protocol_type, status=status)
    return success(resources)


@router.post("/resource/mock", summary="生成资源仿真数据",
             description="逐层获取资源树资源信息", response_model=ApiResponse)
async def mock_resource():
    return success()
