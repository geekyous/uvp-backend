from app.api import user_api, auth_api, device_resource_api, test_data_api


def include_routes(app):
    app.include_router(user_api.router)
    app.include_router(auth_api.router)
    app.include_router(device_resource_api.router)
    app.include_router(test_data_api.router)
