from typing import Optional, Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    successful: str
    resultCode: int
    resultHint: Optional[str]
    resultValue: Optional[Any]


def success(data: Any = None, result_hint="调用成功") -> dict[str, str | int | None | Any]:
    return {
        "successful": "true",
        "resultCode": 200,
        "resultHint": result_hint,
        "resultValue": data
    }


def fail(hint: str = "调用失败", result_code: int = 500) -> dict[str, str | int | None]:
    return {
        "successful": "true",
        "resultCode": result_code,
        "resultHint": hint,
        "resultValue": None
    }
