"""
Game objects inherit Pydantic's BaseModel class to imbue them with 
some useful helper fuctions for sending them over API requests."""

from typing import Any, Dict, List, Match, Optional, Tuple, Type
from abc import ABC
from pydantic import BaseModel, Field


class User(BaseModel):
    """An object with basic user information.

    Attributes:
        id (int): Unique ID for object
        name (str): The user's display name

    """

    id: int
    username: str


class Move(BaseModel):
    """An object containing information about the move and the user

    Attributes:
        parent_command_id (int): UID of the `Command` that initiated a `GetMoveCommand`
        move (str): either "rock", "paper", or "scissors"
        user (User): the `User` submitting the move

    """

    parent_uid: int
    move: str
    # user: User


class State(BaseModel):
    """Base implementation of a State"""

    name: str


class States(BaseModel):
    """A simple dataclass for State definitions"""

    welcome: State = State(name="Welcome")
    req_lobby: State = State(name="Requesting Lobby")
    in_lobby: State = State(name="In Lobby")
    match_request: State = State(name="Requesting Match")
    matched: State = State(name="Matched")
    rejected: State = State(name="Rejected")
    ready: State = State(name="Players Ready?")
    get_move: State = State(name="Submit Moves")
    game_over: State = State(name="Game Over")


class GameState(BaseModel):
    """A complete game state class, indicating the involved users, current game data,
    current game status (pending moves, pending game start, etc), and any other
    information needed to process or rebuild the game's current state, across modules.
    """

    game_id: Optional[int] = None
    state: State = States().welcome
    players: Optional[Tuple[User]] = None
    ready: Optional[Tuple[User]] = None
    current_moves: Optional[Dict[str, Move]] = None
    moves_history: Optional[Tuple[Tuple[Any, Move]]] = None
    winner: Optional[Any] = None

    class Config:
        arbitrary_types_allowed = True

    """
    Okay, what are my game states?

    * Welcome
    * Requesting Lobby
    * Select Opponent
    * Requesting Opponent
        * Matched, begin Game
        * Request Rejected, return to Lobby
    * Game
        * Requesting 'Ready' status from players
        * Waiting for opponent
        * Request 'Move' from players
        * Waiting for opponent
        * Game Over
            * New Game?
            * Return to Lobby
    """


class Command(BaseModel):
    """An instruction packet, generated by Server, consumed by Client.

    Contains instructions that trigger state changes in the UI.
    Should always be subclassed, with more specific information made available
    for each type of Command (display_game_over, await_response, )

    Attributes:
        id (int): Unique ID for object


    Functions:
        execute()
            * contains the functions necessary to trigger change in the client

    """

    uid: int
    command: str
    state: GameState


class Mocks:
    class utils:
        @staticmethod
        def make_mock_GameState(mock):
            return GameState(**mock)

        @staticmethod
        def make_mock_User(mock):
            return User(**mock)

    class mocks:
        users = {
            "user1": {"id": "51", "username": "one o' ya"},
            "user2": {"id": "420", "username": "another 'ya"},
            "me": {"id": 7734, "username": "cbxm"},
        }

        states = {
            "welcome": {
                "game_id": 0,
                "state": States().welcome,
                "players": None,
                "ready": None,
                "current_moves": None,
                "moves_history": None,
                "winner": None,
            },
            "req_lobby": {
                "game_id": 1,
                "state": States().req_lobby,
                "players": None,
                "ready": None,
                "current_moves": None,
                "moves_history": None,
                "winner": None,
            },
            "in_lobby": {
                "game_id": 2,
                "state": States().in_lobby,
                "players": "",
                "ready": "",
                "current_moves": "",
                "moves_history": "",
                "winner": "",
            },
            "match_request": {
                "game_id": 3,
                "state": States().match_request,
                "players": "",
                "ready": "",
                "current_moves": "",
                "moves_history": "",
                "winner": "",
            },
            "matched": {
                "game_id": 4,
                "state": States().matched,
                "players": "",
                "ready": "",
                "current_moves": "",
                "moves_history": "",
                "winner": "",
            },
            "rejected": {
                "game_id": 5,
                "state": States().rejected,
                "players": "",
                "ready": "",
                "current_moves": "",
                "moves_history": "",
                "winner": "",
            },
            "ready": {
                "game_id": 6,
                "state": States().ready,
                "players": "",
                "ready": "",
                "current_moves": "",
                "moves_history": "",
                "winner": "",
            },
            "get_move": {
                "game_id": 7,
                "state": States().get_move,
                "players": "",
                "ready": "",
                "current_moves": "",
                "moves_history": "",
                "winner": "",
            },
            "game_over": {
                "game_id": 8,
                "state": States().game_over,
                "players": "",
                "ready": "",
                "current_moves": "",
                "moves_history": "",
                "winner": "",
            },
        }