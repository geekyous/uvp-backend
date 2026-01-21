import hashlib
import time
from urllib.parse import urlencode

from fastapi import Depends

import app.core.cache as cache
from app.core.exception import AuthException
from app.core.response import fail
from app.core.settings import settings
from app.models.request_params import AuthParams
from app.services.credential import get_secret_by_ak


async def auth_dependency(auth: AuthParams = Depends()):
    """请求校验"""

    ak = auth.ak
    token = auth.token
    timestamp = auth.timestamp
    nonce = auth.nonce

    if not all([ak, token, timestamp, nonce]):
        raise AuthException("鉴权参数缺失")

    try:
        check_timestamp(timestamp)
    except Exception as e:
        raise AuthException(str(e))

    try:
        await check_replay(ak, nonce)
    except Exception as e:
        raise AuthException(str(e))

    token_key = f"token:{token}"
    if not await cache.redis_client.exists(token_key):
        raise AuthException("token无效")

    security_key = get_secret_by_ak(ak)
    if not security_key:
        raise AuthException("AK 无效")

    return None


def check_timestamp(ts: int):
    """时间窗口校验"""
    now = int(time.time())
    if abs(now - ts) > settings.NONCE_TTL_SECONDS:
        return fail(hint="请求已过期")
    return None


async def check_replay(ak: str, nonce: str):
    """防重防校验"""
    nonce_key = f"nonce:{ak}:{nonce}"
    success = await cache.redis_client.set(nonce_key, "1", nx=True, ex=settings.NONCE_TTL_SECONDS)
    if not success:
        return fail(hint="重复请求")
    return None


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
