"""Module for contacting the Server and passing Commands and Game State to the GUI.
"""

from typing import Callable
from obj import IClientCommander


class ConcreteClient:
    class Commands(IClientCommander):
        """Commands that can be issued by the GUI instance.

        These methods must be declared as async methods.
        These methods cannot take any arguments.
        These methods must be static methods.
        """

        def __init__(self, IGUIInterface):
            self.gui = IGUIInterface

        @staticmethod
        async def submit_move():
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

        @staticmethod
        async def _get_game_state():
            """Client functionality to request game state from the server goes here."""
            ...

        @staticmethod
        async def start_game() -> bool:
            """To Dummy this, I'll be returning a mocked static GameState class."""
            request = "some mock data"
            return True