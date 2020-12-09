"""Module for contacting the Server and passing Commands and Game State to the GUI."""

from abc import abstractmethod
from typing import Any, Callable, Coroutine, Dict
import asyncio
import json
from requests import Response, post
from pydantic import BaseModel
from obj import User, GameState


class RPSBeacon:
    # The IP Address of the server hosting our API.
    basepoint: str = "http://127.0.0.1:8000"

    @staticmethod
    def send(endpoint: str = "/", data: dict = None) -> str:
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
        url: str = RPSBeacon.basepoint + endpoint

        # Get the data in literal JSON form.
        jdata: str = json.dumps(data)

        # Use `requests` native post function, and assign the response
        response: Response = post(url=url, data=jdata)

        # Then debug the response...
        print(f"DEBUG : {response = }")

        # ...and return the JSON string of it.
        return response.text

    @staticmethod
    def _request_game_state(user: User) -> GameState:
        """Internal function to assist with a game state request"""
        # Make the request.
        response: str = RPSBeacon.send("/get_game_state", user.dict())

        print(f"DEBUG | {response = }")
        # Convert the JSON response to a dictionary
        state_dict: dict = json.loads(response)

        # And return a fully formed and lovingly recreated GameState object
        return GameState(**state_dict)

    @staticmethod
    def get_game_state(sender: str, data: dict) -> None:
        """Beacon signal to request game state from Server.

        Args:
            sender (str): The DPG element that called the function
            data (dict): A dictionary containing a User and an Injector Callable
        """
        # DEBUG
        print(f"DEBUG | Entering func: `beacon.get_game_state`")
        print(f"DEBUG | {data = }")

        # Extract user and state injector from `data`
        user = data["user"]
        injector = data["__injector"]

        # Do our real job, which is to send a request to the server, and get a response
        state = RPSBeacon._request_game_state(user)

        # And inject that back into the GUI.
        injector(state)

        # fin
        return None


def main():
    pass


if __name__ == "__main__":
    main()

# region  DEPRECATED
''' DEPRECATED.
@staticmethod
def _mock_request(user: User) -> GameState:
    """A stand-in for an IO bound async request"""
    print("Enter RPSBeacon._mock_request")
    mock_state = GameState(**Mocks.states["rejected"])
    print(f"DEBUG : {mock_state.state = }")
    return mock_state
'''
# endregion
