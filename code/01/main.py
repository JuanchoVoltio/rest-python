import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get('/') #Definición del endpoint. La anotación indica que este soportará un método GET
def saludar():
    return "Hola Mundo"

@app.get('?') #TODO: Práctica 2: Definir el path del endpoint
def sumar():
    #TODO: Práctica 2: Implementar la lógica requerida
    pass