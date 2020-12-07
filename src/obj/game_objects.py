"""Game objects are """

from typing import Any, List, Optional, Tuple, Type
from abc import ABC
from pydantic import BaseModel, Field


class Snowflake(ABC):
    """Base class for all game objects.

    Attributes:
        id (int): Unique ID for object


    """

    ...


class Connection(Snowflake):
    """Object for management of socket connection

    Attributes:
        id (int): Unique ID for object
        socket (Socket)
        user (User)

    Functions:
        send_data(data)        # Really necessary?
        send_command(Command)  # Really necessary?


    """

    ...


class Game(Snowflake):
    """A class for housing game logic and managing the game's internal state.

    Attributes:
        id (int): Unique ID for object
        current_state
        move_history
        players_in_game

    Functions:
        get_game_state()
            * return a serializable, file writable, importable save state.
        load_game_state(state_file)
            * restores internal game state from file.
        submit_move(move)

    """

    ...


class User(BaseModel):
    """An object with basic user information.

    Attributes:
        id (int): Unique ID for object
        name (str): The user's display name

    """

    id: int
    username: str
    password: str

    ...


class __GameState(Snowflake):
    """
    Deprecated class. See new GameState
    """

    game_id: int
    player_list: Tuple[User]
    pending_move: Any  # a description of what the game is CURRENTLY waiting on
    history: Any


class Command(Snowflake):
    """An instruction packet, received by client from server.

    Contains instructions that trigger state changes in the UI.
    Should always be subclassed, with more specific information made available
    for each type of Command (display_game_over, await_response, )

    Attributes:
        id (int): Unique ID for object


    Functions:
        execute()
            * contains the functions necessary to trigger change in the client

    """

    ...


# // TODO: Implement below list of commands as subclasses.

# Command List:
# * prompt_move
# * display_result
# * wait_for_result
# * prompt_new_game


class Move(Snowflake):
    """An object containing information about the move and the user

    Attributes:
        id (int): Unique ID for object
        move (str): either "rock", "paper", or "scissors"
        user (User): the `User` submitting the move

    """

    ...


class GameState(BaseModel):
    """A complete game state class, indicating the involved users, current game data,
    current game status (pending moves, pending game start, etc), and any other
    information needed to process or rebuild the game's current state, across modules.
    """

    game_id: Optional[int] = Field(...)
    players: Optional[Tuple[User]]
    state: str = "Welcome"
    submitted_moves: Optional[Tuple[Tuple[User, Move]]]

    class Config:
        arbitrary_types_allowed = True
