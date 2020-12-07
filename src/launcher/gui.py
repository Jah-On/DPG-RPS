# DEBUG
from typing import Callable
import dearpygui.core as core
import dearpygui.simple as simple
from client.client import RPSBeacon
from obj import IClientCommander, IGUI
from obj.game_objects import GameState, User


class GUI:
    class Commands:
        """Commands exposed to the Client instance"""

        @staticmethod
        def inject_game_state(state: GameState):
            core.add_data("__active.state", state)

        @staticmethod
        def consume_game_state(sender, data):
            """This function interprets the game state and builds the GUI accordingly"""
            print("enter GUI.Commands.consume_game_state")
            try:
                game_state = core.get_data("__active.state")
                print(game_state)
                core.add_text(game_state["state"], parent="Main")
            except Exception as e:
                print(e)

        @staticmethod
        async def request_game_state(sender, data):
            """
            docstring
            """
            print("enter GUI.Commands.request_game_state")
            print(f"{sender = }")
            print(f"{data = }")
            print()
            beacon = core.get_data("beacon")
            user = core.get_data("user")
            data = {
                "user": user,
                "injector": GUI.Commands.inject_game_state,
                "beacon": beacon,
            }
            print()
            print(beacon, "\n", user)
            print()
            print("data = \n", data["user"])

            async def f(*args, **kwargs):
                print(args)
                print(kwargs)
                print("enter f")

            # This function is where it's broken.
            core.run_async_function(
                f,
                data,
                return_handler=GUI.Commands.consume_game_state,
            )

    async def __init__(self, Beacon: RPSBeacon):
        # Create our beacon
        self.beacon = Beacon()
        fake_state = {"state": "fake"}
        core.add_data("__active.state", fake_state)
        user = User(id=7734, username="cbxm", password="passwordy")
        core.add_data("user", user)

        # Stash it in DPG's data store
        core.add_data("beacon", self.beacon)

        # self.commands.get_game_state_to_target(self.Commands.inject_game_state)

        # Init the welcome screen
        await self.main()

    async def main(self):
        with simple.window("Main"):
            core.add_text("Hello World!")
            await self.welcome_screen()
        core.set_primary_window("Main", True)
        core.add_button(
            "Request GameState",
            parent="Main",
            callback=GUI.Commands.request_game_state,
            callback_data="mock data" + "moremockdata",
        )
        # self.Commands.consume_game_state(sender=None, data=None)

    async def _consume_game_state(self, state):
        ...

    async def welcome_screen(self):
        core.add_text("Welcome to DPG-RPS This is the Welcome screen!", parent="Main")
        core.add_button("Start Game")

    def start_gui(self):
        """Simple method for exposing the GUI lift-off command"""
        core.start_dearpygui()
