from fastapi import APIRouter

from app.core.response import success
from app.models.request_params import QueryResource
from app.models.request_respones import QueryResourcesVO

router = APIRouter(prefix="/uvp-backend-common/api/v1")


@router.post("/resource/queryResources", tags=["资源服务"], summary="逐层查询资源树信息",
             description="逐层获取资源树资源信息")
async def query_resources(query_request=QueryResource):
    return success(
        QueryResourcesVO(
            id="b26c9ae118e44bb1aaf64742cc2b1fe2",
            text="图片机21",
            devShortName="",
            pNotes=None,
            pCode=None,
            url=None,
            openType=0,
            pid="8111d03baaed4a00a9ef6a48fd935d04",
            path="南京/输电/南瑞路/图片机21",
            type=0,
            isGroup=0,
            isAvailable=1,
            order=3322,
            hasChildren=False,
            status=1,
            isOuternet=0,
            sDecodeTag="100",
            devCode="100110000003090014",
            devType="09",
            lng=None,
            lat=None,
            childrenCount=0,
            gisPeerCode=None,
            childNodes=[],
            sysInfoCode=None,
            dvrCode=None,
            isCheck=False,
            fontTypeCode=None,
            peerId=None,
            audio=None,
        ))
