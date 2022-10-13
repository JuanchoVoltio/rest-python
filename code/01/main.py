import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get('/')
def saludar():
    return "Hola Mundo"
