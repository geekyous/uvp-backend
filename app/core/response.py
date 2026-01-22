from typing import Optional, Any

from pydantic import BaseModel
from starlette.responses import JSONResponse


class ApiResponse(BaseModel):
    successful: str
    resultCode: int
    resultHint: Optional[str]
    resultValue: Optional[Any]


def success(data: Any = None, result_hint="调用成功") -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content=ApiResponse(
            successful="true",
            resultCode=200,
            resultHint=result_hint,
            resultValue=data
        ).model_dump()
    )


def fail(hint: str = "调用失败", result_code: int = 500) -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content=ApiResponse(
            successful="true",
            resultCode=result_code,
            resultHint=hint,
            resultValue=None
        ).model_dump()
    )
