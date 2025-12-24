from fastapi import APIRouter

from app.core.response import success, fail
from app.models.auth_request import AuthRequest
from app.services.auth_service import create_token, validate_token
from app.services.credential import get_secret_by_ak

router = APIRouter(prefix="/uvp-backend-common/api/v1")


@router.post("/authorization", tags=["应用集成授权"],
             summary="应用授权",
             description="""
             根据应用集成的AK与SK，获取请求授权Token，Token默认访问有效期为30分钟。应用授权后，在有效时间内可以重复使用Token，请勿频繁授权。
             """)
async def authorization(auth_req: AuthRequest):
    ak = auth_req.ak
    sk = auth_req.sk
    if ak is None or sk is None:
        return fail("AK/SK 不能为空")
    security_key = await get_secret_by_ak(ak)
    if not security_key or security_key != sk:
        return fail("AK/SK 无效")
    token = await create_token(ak)
    return success({
        "ak": ak,
        "token": token
    })


@router.post("/validateToken", tags=["应用集成授权"],
             summary="token验证",
             description="验证token是否有效。过期或无效返回0，有效则返回过期时间（单位：秒）")
async def validate_token_api(token: str):
    ttl = await validate_token(token)
    return success(ttl)
