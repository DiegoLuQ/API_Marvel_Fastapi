from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.apis.base import api_router
from webapps.base import api_router as webapp_router

def include_router(app):
    app.include_router(api_router)
    app.include_router(webapp_router)

def configure_router(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_aplitacion():
    app = FastAPI()
    include_router(app)
    configure_router(app)
    return app

app = start_aplitacion()

@app.get('/')
def hello_api():
    return {"detail":"HelloWorld"}