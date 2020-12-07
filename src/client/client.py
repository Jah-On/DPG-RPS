"""Module for contacting the Server and passing Commands and Game State to the GUI."""

from abc import abstractmethod
from typing import Any, Coroutine
import json
from requests import Response, post
from pydantic import BaseModel

# from obj.game_objects import User
# from obj import IClientCommander

basic_data = {
    "id": 0,
    "request": "okay",
}

'''
class ConcreteClient:
    class Commands(IClientCommander):
        """Commands that can be issued by the GUI instance.

        These methods must be declared as async methods.
        These methods cannot take any arguments.
        These methods must be static methods.
        """

        def __init__(self):
            ...

        @staticmethod
        async def submit_generic(scope, receive, send):
            assert scope["type"] == "http"
            request = Request(scope, receive)
            content = f"{request.method} {request.url.path}"
            response = Response(content, media_type="text/plain")
            await response(scope, receive, send)

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
'''


class User(BaseModel):
    """An object with basic user information.

    Attributes:
        id (int): Unique ID for object
        name (str): The user's display name

    """

    id: int
    username: str
    password: str


class RPSBeacon:
    def __init__(self, basepoint: str = "http://127.0.0.1:8000"):
        self.basepoint = basepoint

    async def get(self, endpoint: str = "/", data: dict = None) -> str:
        """Most basic of interfaces for sending a request to the server.

        Args:
            endpoint (str): API endpoint to send command to. Requires leading '/'.
            data (dict): A Python dictionary, formable into valid JSON request.

        Note:
            `get()` does not do any data validation whatsoever. This is the most very
            most basic of interfaces, and requires some beefing up before it
            goes to production. Underscore prefix indicates that this is meant as an
            internal tool only.

        Returns:
            str: A str object, theoretically as formed JSON, convertable to dict.
        """
        url = self.basepoint + endpoint
        jdata = json.dumps(data)

        response = post(url=url, data=jdata)
        return response.text

    async def _get_game_state(self, user: User) -> Coroutine[Any, Any, str]:
        response = self.get("/get_game_state", user.dict())
        return response

    async def get_game_state(self, sender, data):
        print("enter beacon.get_game_state")
        user = data["user"]
        injector = data["injector"]
        state = self._get_game_state(user)
        injector(state)


def main():
    ...


if __name__ == "__main__":
    main()
