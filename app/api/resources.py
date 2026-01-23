from fastapi import APIRouter, Depends

from app.core.response import success, ApiResponse
from app.core.security import auth_dependency
from app.models.request_params import QueryResource
from app.services.resources_service import get_resource, mock_device_resource

router = APIRouter(prefix="/uvp-backend-common/api/v1", tags=["资源服务"], dependencies=[Depends(auth_dependency)], )


@router.post("/resource/queryResources", summary="逐层查询资源树信息",
             description="逐层获取资源树资源信息", response_model=ApiResponse)
async def query_resources(query_request: QueryResource):
    dev_type = query_request.devType
    status = query_request.status
    pid = query_request.pid
    protocol_type = query_request.protocolType
    resource_list = await get_resource(pid, dev_type, protocol_type, status)
    return success(resource_list)


@router.post("/resource/mock", summary="生成资源仿真数据",
             description="逐层获取资源树资源信息", response_model=ApiResponse)
async def mock_resource():
    await mock_device_resource()
    return success()
