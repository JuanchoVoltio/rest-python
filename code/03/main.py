from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    nombre: str
    descripción: Union[str, None] = "N/A" #Asignar un valor por omisión del campo.
    precio_base: float
    descuento: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    precio_final = item.precio_base * (1 - item.descuento/100)
    return {"item": item, "precio": precio_final}
