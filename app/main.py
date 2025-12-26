import asyncio

import uvicorn
from fastapi import FastAPI, Request

from app.core.log.config import setup_logging

setup_logging()
from app.api import auth
from app.core.lifespan import lifespan

from app.core.log.middleware import RequestIDMiddleware
from app.core.security import verify_request

app = FastAPI(
    title="UVP平台服务目录",
    description="UVP平台服务目录测试接口",
    lifespan=lifespan)

app.add_middleware(RequestIDMiddleware)
app.include_router(auth.router)


@app.middleware("http")
async def security_middleware(request: Request, call_next):
    public_paths = [
        "/docs",
        "/openapi.json",
        "/redoc",
        "/docs/oauth2-redirect",
    ]
    # 跳过 swagger openai
    if request.url.path in public_paths:
        return await call_next(request)

    if request.url.path.endswith(("authorization", "validateToken")):
        return await call_next(request)

    error = await verify_request(request)
    if error:
        return error
    return await call_next(request)


async def main():
    """异步主函数"""
    config = uvicorn.Config(
        app=app,
        host="127.0.0.1",
        port=8000,
        log_level="info",
        loop="asyncio"
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
