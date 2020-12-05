"""Module for contacting the Server and passing Commands and Game State to the GUI.
"""

from typing import Callable
from obj import IClientCommander


class Client:
    class Commands(IClientCommander):
        @staticmethod
        def func():
            ...

        @staticmethod
        def submit_move():
            pass

        @staticmethod
        async def get_game_state_to_target(target: Callable) -> None:
            """Requests game state from Server and passes it back via parameter function.

            Args:
                target (Callable): A function that takes one argument: the game state.
            Raises:
                Exception
            """
            pass
