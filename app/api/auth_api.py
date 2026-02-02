import logging

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.response import fail, success
from app.schemas.auth_params import AuthRequest, ValidateTokenRequest
from app.services.token_service import TokenService

router = APIRouter(prefix="/uvp-backend-common/api/v1", tags=["应用集成授权"], )

logger = logging.getLogger(__name__)


@router.post("/authorization",
             summary="应用授权",
             description="""
             根据应用集成的AK与SK，获取请求授权Token，Token默认访问有效期为30分钟。应用授权后，在有效时间内可以重复使用Token，请勿频繁授权。
             """)
async def authorization(auth_req: AuthRequest, db: AsyncSession = Depends(get_db)):
    ak = auth_req.ak
    sk = auth_req.sk
    if ak is None or sk is None:
        return fail(hint="AK/SK 不能为空")
    security_key = await TokenService.get_secret_by_ak(db, ak)
    if not security_key or security_key != sk:
        return fail(hint="AK/SK 无效")

    token = await TokenService.create_token(ak)
    return success({
        "ak": ak,
        "token": token
    })


@router.post("/validateToken",
             summary="token验证",
             description="验证token是否有效。过期或无效返回0，有效则返回过期时间（单位：秒）")
async def validate_token_api(token_req: ValidateTokenRequest):
    ttl = await TokenService.validate_token(token_req.token)
    return success(ttl)
