from pydantic import BaseModel

class Imagen(BaseModel):
    path :str
    extension: str
class MarvelChars(BaseModel):
    nombre: str
    descripcion: str
    comics_disponibles: str
    series_disponibles: str
    imagen : Imagen