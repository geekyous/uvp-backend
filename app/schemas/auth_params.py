import time

from fastapi import Query
from pydantic import Field

from app.models.base import CamelModel


class AuthParams(CamelModel):
    ak: str = Query(..., description="AccessKey")
    token: str = Query(..., description="访问令牌")
    nonce: str = Query(..., description="随机数")
    timestamp: float = Query(time.time(), description="时间戳")


class AuthRequest(CamelModel):
    """应用授权接口参数"""
    sk: str
    ak: str


class ValidateTokenRequest(CamelModel):
    token: str = Field(..., description="token")
