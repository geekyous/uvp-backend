import asyncio
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse

from app.core.lifespan import lifespan
from app.core.logger import setup_logging
from app.core.response import ApiResponse
from app.exceptions.exceptions import AuthException, BizException
from app.core.routers import include_routes

setup_logging()

app = FastAPI(
    title="UVP平台服务目录",
    description="UVP平台服务目录测试接口",
    lifespan=lifespan
)

# 前端和后端在同一端口，不需要 CORS 中间件
# 如需跨域访问，请取消注释以下配置

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:8080",
#         "http://127.0.0.1:8080",
#         "null"  # 允许所有来源
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

include_routes(app)

# 挂载静态文件目录
app.mount("/web", StaticFiles(directory="app/web"), name="web")


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
