from fastapi import Query, Body

from app.models.base import CamelModel


class AuthParams(CamelModel):
    ak: str = Query(..., description="AccessKey")
    token: str = Query(..., description="访问令牌")
    nonce: str = Query(..., description="随机数")
    timestamp: str = Query(..., description="时间戳")
    cookie: str | None = Query(None, description="cookie")


class AuthRequest(CamelModel):
    """应用授权接口参数"""
    sk: str = Body(..., description="sk", title="SecretKey")
    ak: str = Body(..., description="ak", title="AccessKey")


class ValidateTokenRequest(CamelModel):
    token: str = Body(..., description="token")
