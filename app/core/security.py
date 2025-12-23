import time

from fastapi import Request

import app.core.cache as cache
from app.core.config import settings
from app.core.response import fail


async def verify_request(request: Request):
    """请求校验"""
    headers = request.headers

    ak = headers.get("ak")
    token = headers.get("token")
    timestamp = headers.get("timestamp")
    nonce = headers.get("nonce")

    if not all([ak, token, timestamp, nonce]):
        return fail("鉴权参数缺失")

    now = int(time.time())
    if abs(now - int(timestamp)) > 300:
        return fail("请求已过期")

    nonce_key = f"nonce:{ak}:{nonce}"
    if cache.redis_client.exists(nonce_key):
        return fail("重复请求")

    await cache.redis_client.setex(nonce_key, settings.NONCE_TTL_SECONDS, "1")

    token_key = f"token:{token}"
    if not cache.redis_client.exists(token_key):
        return fail("token无效")

    return None
