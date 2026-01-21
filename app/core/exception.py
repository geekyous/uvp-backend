from fastapi import Request

from app.core.response import fail
from app.main import app


class BizException(Exception):
    """业务异常"""

    def __init__(self, message: str):
        self.message = message


class AuthException(Exception):
    """鉴权异常"""

    def __init__(self, message: str):
        self.message = message


@app.exception_handler(AuthException)
async def auth_exception_handler(request: Request, exc: AuthException):
    return fail(hint=str(exc))


@app.exception_handler(BizException)
async def biz_exception_handler(request: Request, exc: BizException):
    return fail(hint=str(exc))
