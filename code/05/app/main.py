import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Perro(BaseModel):
    id: Optional[int] = None
    nombre: str
    edad: int
    raza: str


with open('/code/./app/datos-perros.json', 'r') as archivo_perros: #Lo usaremos para el despliegue en docker
#with open('datos-perros.json', 'r') as archivo_perros:
    perritos = json.load(archivo_perros)['perritos']


@app.get('/perritos/{id}')
def ver_perrito(id: int):
    perrito = [perrito for perrito in perritos if perrito['id'] == id]
    if(len(perrito) > 0):
        return perrito[0]
    else:
     raise HTTPException(status_code=404, detail="No se encontró un perrito con id {0}".format(id))

