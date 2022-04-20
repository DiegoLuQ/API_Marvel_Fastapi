import os
import requests
import time
from json import loads
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
ts = 1
private_key = os.getenv('PRIVATE_KEY')
public_key = os.getenv('PUBLIC_KEY')
hashed = os.getenv('HASHED')


def get_json(limit, offset):
    # start_time = time.time()
    url = f"https://gateway.marvel.com:443/v1/public/characters?limit={limit}&offset={offset}&ts={ts}&apikey={public_key}&hash={hashed}"
    response = requests.get(url)
    if response.status_code == 200:
        response_json = loads(response.text)
        db_marvel = []
        for i in response_json["data"]["results"]:
            nombre = i["name"]
            descripcion = i["description"]
            imagen = i["thumbnail"]
            comics_disponibles = i["comics"]["available"]
            series_disponibles = i["series"]["available"]
            dict_marvel = {"nombre":nombre, "descripcion":descripcion, "comics_disponibles":comics_disponibles, "series_disponibles":series_disponibles, "imagen":imagen}
            db_marvel.append(dict_marvel)
            end_time = time.time()
            
        # total_time = end_time - start_time
        # print(total_time)
        return db_marvel

def get_json_limit10():
    # start_time = time.time()
    url = f"https://gateway.marvel.com:443/v1/public/characters?limit=10&offset=1&ts={ts}&apikey={public_key}&hash={hashed}"
    response = requests.get(url)
    if response.status_code == 200:
        response_json = loads(response.text)
        db_marvel = []
        for i in response_json["data"]["results"]:
            nombre = i["name"]
            descripcion = i["description"]
            imagen = i["thumbnail"]
            comics_disponibles = i["comics"]["available"]
            series_disponibles = i["series"]["available"]
            dict_marvel = {"nombre":nombre, "descripcion":descripcion, "comics_disponibles":comics_disponibles, "series_disponibles":series_disponibles, "imagen":imagen}
            db_marvel.append(dict_marvel)
            end_time = time.time()
            
        # total_time = end_time - start_time
        # print(total_time)
        return db_marvel