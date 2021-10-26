from fastapi import FastAPI
from app.config import Config


def create_app():
    app_ = FastAPI(title=Config.PROJECT_NAME)

    from app.routers import check_health

    base_path = f"/{Config.API_NAME}"

    app_.include_router(check_health.api_router, prefix=base_path)

    return app_
