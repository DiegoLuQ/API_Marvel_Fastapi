from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from core.functions.main import get_json_limit10

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")


@router.get('/')
def home(request: Request):
    return templates.TemplateResponse("home.html",{"request":request})

@router.get('/list-chars')
def list_char(request:Request):
    data_chars = get_json_limit10()
    return templates.TemplateResponse("characters/homechars.html", {"request":request, "title":"Listado de Marrvel", "data":data_chars})