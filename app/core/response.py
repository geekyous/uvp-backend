from typing import Any, Optional, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    successful: bool
    resultCode: int
    resultHint: Optional[str] = None
    resultValue: Optional[Any] = None


def success(
        data: T | None = None,
        result_hint: str = "调用成功",
) -> ApiResponse[T]:
    return ApiResponse(
        successful=True,
        resultCode=200,
        resultHint=result_hint,
        resultValue=data,
    )


def fail(
        result_hint: str = "调用失败",
        result_code: int = 500,
) -> ApiResponse[None]:
    return ApiResponse(
        successful=False,
        resultCode=result_code,
        resultHint=result_hint,
        resultValue=None,
    )
