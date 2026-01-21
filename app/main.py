import asyncio

import uvicorn
from fastapi import FastAPI

from app.core.log.config import setup_logging

setup_logging()
from app.api import auth, resources
from app.core.lifespan import lifespan

from app.core.log.middleware import RequestIDMiddleware

app = FastAPI(
    title="UVP平台服务目录",
    description="UVP平台服务目录测试接口",
    lifespan=lifespan)

app.add_middleware(RequestIDMiddleware)
app.include_router(auth.router)
app.include_router(resources.router)


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
