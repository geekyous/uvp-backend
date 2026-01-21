from typing import Optional, Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    successful: str
    resultCode: int
    resultHint: Optional[str]
    resultValue: Optional[Any]


def success(data=None, hint="调用成功"):
    return ApiResponse(
        successful="true",
        resultValue=data,
        resultHint=hint,
        resultCode=200
    )


def fail(result_code=500, hint="调用失败"):
    return ApiResponse(
        successful="false",
        resultValue=None,
        resultHint=hint,
        resultCode=result_code
    )
