"""The `obj` module contains ABCs and Interface definitions for the application."""

from typing import Callable
from abc import ABC, abstractmethod


class ICommand(ABC):
    """Base class for an individual command."""

    @staticmethod
    @abstractmethod
    def __call__() -> None:
        """Akin to implementing an `execute` function.

        Every command (which is an object) must also be a callable.
        """
        raise NotImplementedError


class IClientCommander(ABC):
    """A Commander object, containing all commands the GUI can implement."""

    class RequestLobby(ICommand):
        pass

    class SubmitMove(ICommand):
        pass

    class RequestStartGame(ICommand):
        pass

    @staticmethod
    @abstractmethod
    async def request_start_game():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def submit_move():
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def get_game_state_to_target(target: Callable) -> None:
        """Requests game state from Server and passes it back via parameter function.

        Args:
            target (Callable): A function that takes one argument: the game state.
        Raises:
            Exception
        """
        raise NotImplementedError


class IGUI(ABC):
    """Interface for the GUI commands that the Client needs access to."""

    @staticmethod
    @abstractmethod
    def inject_game_state(state):
        raise NotImplementedError
