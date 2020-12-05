from . import Move, User, Game, Command, Connection
from typing import List, Union


def authenticate(user: str, pw: str) -> User:
    return User


def submit_move(move: Move, user: User) -> bool:
    """API function to submit a move to the server.

    Args:
        move (Move): Either "Rock", "Paper", or "Scissors"
        user (User): The User object of the sender

    Returns:
        bool: True if successful, False if otherwise.

    Raises:
        InvalidMoveException: Error if submitted move is invalid.

    """

    ...


def register_new_user(username: str, pw: str) -> User:
    """API function to submit a new user registration.

    Args:
        username (str): No special characters, no whitespace, 20 char limit.
        pw (str): 8 char minimum.

    Returns:
        bool: True if successful,
    """
    return User


def request_connection() -> Union[Connection, bool]:
    ...


def request_available_players(user: User) -> bool:
    return False


def request_connection_with_player(user: User) -> Connection:
    return Connection