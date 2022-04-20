from fastapi import APIRouter

from core.apis.version1 import route_chars


api_router = APIRouter()

api_router.include_router(
    route_chars.router,
    prefix="/marvel-chars",
    tags=["Characters"]
)