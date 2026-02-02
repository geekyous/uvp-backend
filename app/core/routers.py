from app.api import user_api, auth_api, resource_api


def include_routes(app):
    app.include_router(user_api.router)
    app.include_router(auth_api.router)
    app.include_router(resource_api.router)
