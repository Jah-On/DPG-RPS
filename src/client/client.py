"""Module for contacting the Server and passing Commands and Game State to the GUI."""

from abc import abstractmethod
from typing import Any, Callable, Coroutine, Dict
import asyncio
import json
from requests import Response, post
from pydantic import BaseModel
from obj.game_objects import User, GameState, Mocks


class RPSBeacon:
    def __init__(self, basepoint: str = "http://127.0.0.1:8000"):
        self.basepoint = basepoint

    async def send(self, endpoint: str = "/", data: dict = None) -> str:
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

        # From our basepoint, construct a fully-qualified endpoint URL
        url = self.basepoint + endpoint

        # Get the data in literal JSON form.
        jdata = json.dumps(data)

        # Use `requests` native post function, and assign the response
        response = post(url=url, data=jdata)

        # Then debug the response...
        print(f"DEBUG : {response = }")

        # ...and return the content of it.
        return response.text

    async def _request_game_state(self, user: User) -> str:
        """Internal function to assist with a game state request"""
        response = await self.send("/get_game_state", user.dict())
        return response

    def _mock_request(self, user: User) -> GameState:
        """A stand-in for an IO bound async request"""
        print("Enter RPSBeacon._mock_request")
        mock_state = GameState(**Mocks.states["rejected"])
        print(f"DEBUG : {mock_state.state = }")
        return mock_state

    def get_game_state(self, user: User) -> GameState:
        """Beacon Signal to request game state from Server.

        Args:
            sender: The DPG element that called the function
            data: A dictionary containing a User and a Callable to send data back to DPG
        """
        # DEBUG
        print(f"DEBUG | Entering func: `beacon.get_game_state`")
        print(f"DEBUG | {user = }")

        # Await the game state request
        # Using a dummy request here,
        state = self._mock_request(user)

        # And send it to the GUI.
        return state


def main():
    pass


if __name__ == "__main__":
    main()
