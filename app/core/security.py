import hashlib
import time
from urllib.parse import urlencode

from fastapi import Depends

from app.core import cache
from app.core.config import settings
from app.core.database import get_db
from app.exceptions.exceptions import AuthException
from app.schemas.auth_params import AuthParams
from app.services.token_service import TokenService


async def auth_dependency(auth: AuthParams = Depends()):
    """请求校验"""

    ak = auth.ak
    token = auth.token
    timestamp = auth.timestamp
    nonce = auth.nonce

    if not all([ak, token, timestamp, nonce]):
        raise AuthException("鉴权参数缺失")

    check_timestamp(timestamp)

    await check_replay(ak, nonce)

    token_key = f"token:{token}"
    if not await cache.get_redis().exists(token_key):
        raise AuthException("token无效")

    security_key = await TokenService.get_secret_by_ak(get_db(), ak)
    if not security_key:
        raise AuthException("AK 无效")


def check_timestamp(ts: float):
    """时间窗口校验"""
    now = int(time.time())
    if abs(now - ts) > settings.NONCE_TTL_SECONDS:
        raise AuthException("请求已过期")


async def check_replay(ak: str, nonce: str):
    """防重防校验"""
    nonce_key = f"nonce:{ak}:{nonce}"
    success = await cache.get_redis().set(nonce_key, "1", nx=True, ex=settings.NONCE_TTL_SECONDS)
    if not success:
        raise AuthException("重复请求")


def verify_sign(secret_key: str, query: dict, body: dict):
    """校验签名"""
    sign = query.get("sign")
    data = {}

    for k, v in query.items():
        if k == "sign":
            data[k] = v

    if isinstance(body, dict):
        data.update(body)

    sorted_items = sorted(data.items())
    raw = urlencode(sorted_items)
    raw_string = f"{raw}{secret_key}"
    expected_sign = hashlib.sha256(raw_string.encode()).hexdigest()
    return expected_sign == sign
