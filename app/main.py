import asyncio

import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from app.core.lifespan import lifespan
from app.core.logger import setup_logging
from app.core.response import ApiResponse
from app.exceptions.exceptions import AuthException, BizException

setup_logging()
from app.core.routers import include_routes

app = FastAPI(
    title="UVP平台服务目录",
    description="UVP平台服务目录测试接口",
    lifespan=lifespan
)

include_routes(app)


@app.exception_handler(AuthException)
async def auth_exception_handler(request: Request, exc: AuthException):
    return JSONResponse(
        status_code=401,
        content=ApiResponse(
            successful=True,
            resultCode=200,
            resultHint=str(exc),
            resultValue=None
        ).model_dump()
    )


@app.exception_handler(BizException)
async def biz_exception_handler(request: Request, exc: BizException):
    return JSONResponse(
        status_code=200,
        content=ApiResponse(
            successful=True,
            resultCode=500,
            resultHint=str(exc),
            resultValue=None
        ).model_dump()
    )


async def main():
    """异步主函数"""
    config = uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
        loop="asyncio"
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
