from time import sleep
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from pydantic.errors import StrError

from obj import User, GameState, Mocks


app = FastAPI()


@app.post("/")
async def root():
    return "Hello World!"


@app.post("/get_game_state")
async def get_game_state(user: User) -> GameState:
    print("beginning wait...")
    sleep(10)
    print("done waiting, returning string!")
    gs = Mocks.make_gs("in_lobby")
    return gs
