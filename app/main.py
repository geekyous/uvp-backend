import uvicorn
from fastapi import FastAPI, Request

from app.api import auth
from app.core.security import verify_request

app = FastAPI(
    title="UVP平台服务目录",
    description="UVP平台服务目录测试接口")

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
