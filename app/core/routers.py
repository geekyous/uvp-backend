from app.api import auth, resources
from app.core.log.middleware import RequestIDMiddleware


def include_routes(app):
    app.add_middleware(RequestIDMiddleware)
    app.include_router(auth.router)
    app.include_router(resources.router)
