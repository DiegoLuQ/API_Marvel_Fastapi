from fastapi import APIRouter
from .characters import route_chars

api_router = APIRouter()

api_router.include_router(
    route_chars.router,
    prefix="",
    tags=["List of Characters"]
)