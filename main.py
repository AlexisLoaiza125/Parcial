from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum, auto
from datetime import date


app = FastAPI()

class PosicionFutbol(Enum):
    PORTERO = auto()
    DEFENSA = auto()
    MEDIOCAMPISTA = auto()
    DELANTERO = auto()
    EXTREMO = auto()

class jugador(BaseModel):
    id:int
    name:str
    dorsal:int
    nacimiento:date
    posicion:PosicionFutbol
    altura:float
    equipo:str

jugadores = [
    jugador (id=1, name="messi", dorsal=5, nacimiento="1985-10-31", posicion=PosicionFutbol.DELANTERO, altura=1.50,equipo="barca"),
    jugador (id=2, name="ronaldo", dorsal=7, nacimiento="1985-08-05", posicion=PosicionFutbol.DELANTERO, altura = 1.84, equipo="realmadrid"),
    jugador (id=3, name="ramos", dorsal=1, nacimiento="1993-01-25", posicion=PosicionFutbol.DEFENSA, altura=1.90, equipo="realmadrid"),
    jugador (id=4, name="yamal", dorsal=6, nacimiento="2006-06-12", posicion=PosicionFutbol.EXTREMO, altura=1.70, equipo="barca"),
    jugador (id=5, name="ospina",dorsal=8,nacimiento=1979-11-12,posicion=PosicionFutbol.PORTERO,altura=1.86,equipo="colombia"),
    jugador (id=6, name="Alexis",dorsal=10,nacimiento="2005-01-25",posicion=PosicionFutbol.EXTREMO,altura=1.71,equipo="barca")
    ]

@app.get("/show_one_player/{id}")
def show_player(id:int):
    for jugador in jugadores:
        if jugador.id == id:
            return jugador
    return ("no encontrado")

@app.get("/comparar/{id1}/{id2}")
def comparar(id1: int, id2: int):
    jugador1 = None
    jugador2 = None

    for jugador in jugadores:
        if jugador.id == id1:
            jugador1 = jugador
        if jugador.id == id2:
            jugador2 = jugador

    if jugador1 is None or jugador2 is None:
        return {"error": "uno o ambos jugadores no encontrados"}

    return {
        "jugador1": jugador1,
        "jugador2": jugador2,
        "comparacion": {
            "misma_posicion": jugador1.posicion == jugador2.posicion,
            "mas_alto": jugador1.name if jugador1.altura > jugador2.altura else jugador2.name,
            "misma_equipo": jugador1.equipo == jugador2.equipo
        }
    }

@app.get("/equipo_jugador/{id}")
def equipo_jugador(id: int):
    for jugador in jugadores:
        if jugador.id == id:
            return {
                "jugador": jugador.name,
                "equipo": jugador.equipo
            }
    return {"error": "jugador no encontrado"}

@app.get("/jugadores")
def mostrar_jugadores():
    return jugadores