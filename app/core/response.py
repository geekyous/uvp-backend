from typing import Any, Optional

from pydantic import BaseModel


class ApiResponse(BaseModel):
    successful: str
    resultValue: Optional[Any] = None
    resultHint: str


def success(data=None, hint="调用成功"):
    return ApiResponse(
        successful="true",
        resultValue=data,
        resultHint=hint
    )


def fail(hint="调用失败"):
    return ApiResponse(
        successful="false",
        resultValue=None,
        resultHint=hint
    )
