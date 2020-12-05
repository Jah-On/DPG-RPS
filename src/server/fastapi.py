from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World!"


@app.get("/game_state")
async def get_game_state():
    return False


@app.post("/submit_move")
async def submit_move():
    return False
