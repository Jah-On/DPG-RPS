from time import sleep
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from pydantic.errors import StrError

from obj.game_objects import User


class BaseRequest(BaseModel):
    id: int
    request: str


class StateRequest(BaseModel):
    ...


class GameState(BaseModel):
    state: str


app = FastAPI()


@app.post("/")
async def root():
    return "Hello World!"


@app.post("/generic")
async def receive_generic(request: BaseRequest):
    print(request.id, request.request)
    request.request = "Not anymore!"
    return request


@app.post("/get_game_state")
async def get_game_state(user: User) -> GameState:
    print("beginning wait...")
    sleep(10)
    print("done waiting, returning string!")
    gs = GameState(state="Hey smooth operator")
    return gs
