from fastapi import APIRouter
from core.schemas.chars import MarvelChars
from typing import List
#modulos
from core.functions import main
from webapps.base import api_router as webapp_router 


router = APIRouter()

@router.get('/home', response_model=List[MarvelChars])
def home(limit: int, offset: int):
    return main.get_json(limit, offset)
