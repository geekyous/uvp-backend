import hashlib
import time
from urllib.parse import urlencode

from fastapi import Request

import app.core.cache as cache
from app.core.settings import settings
from app.core.response import fail
from app.services.credential import get_secret_by_ak


async def verify_request(request: Request):
    """请求校验"""
    query = request.query_params

    ak = query.get("ak")
    token = query.get("token")
    timestamp = query.get("timestamp")
    nonce = query.get("nonce")
    cookie = query.get("cookie")

    if not all([ak, token, timestamp, nonce]):
        return fail("鉴权参数缺失")

    try:
        check_timestamp(timestamp)
    except Exception as e:
        return fail(str(e))

    try:
        await check_replay(ak, nonce)
    except Exception as e:
        return fail(str(e))

    token_key = f"token:{token}"
    if not cache.redis_client.exists(token_key):
        return fail("token无效")

    try:
        body = await request.json()
    except Exception:
        body = {}

    security_key = get_secret_by_ak(ak)
    try:
        verify_sign(security_key, query, body)
    except Exception as e:
        return fail(str(e))

    return None


def check_timestamp(timestamp: str):
    """时间窗口校验"""
    try:
        ts = int(timestamp)
    except ValueError:
        raise RuntimeError("timestamp 非法")
    now = int(time.time())
    if abs(now - ts) > settings.NONCE_TTL_SECONDS:
        raise RuntimeError("请求已过期")


async def check_replay(ak: str, nonce: str):
    """防重防校验"""
    nonce_key = f"nonce:{ak}:{nonce}"
    success = await cache.redis_client.set(nonce_key, "1", nx=True, ex=settings.NONCE_TTL_SECONDS)
    if not success:
        raise RuntimeError("重复请求")


def verify_token(token: Request):
    pass


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
