from time import sleep
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.errors import StrError

from obj.objects import User, GameState, Mocks

app = FastAPI()


@app.post("/")
async def root():
    return "Hello World!"


@app.post("/get_game_state")
async def get_game_state(user: User) -> GameState:

    print("beginning false wait...")
    sleep(5)
    print("done waiting, returning string!")

    gs = Mocks.make_gs("in_lobby")

    return gs
