from typing import Callable

import dearpygui.core as core
import dearpygui.simple as simple
from client import RPSBeacon
from obj import GameState, Mocks, User


class GUI:
    def __init__(self, beacon: RPSBeacon):
        # Create our beacon
        self.beacon = beacon

        # Stash the beacon in the data store, also.
        # This allows isolated callback functions to access this, without needing to
        # weave a `Callable` through the callback system.
        core.add_data("beacon", self.beacon)

        # Generate some fake data to use in the application.
        fake_state = Mocks.make_gs(name="matched")
        core.add_data("__active_state", fake_state)
        user = User(id=7734, username="cbxm", password="passwordy")
        core.add_data("user", user)

        # Dynamically generate static methods to be used as callbacks
        # This grants our Beacon instance a .commands namespace.
        self.grant_cmds()

        # Create the welcome screen
        self.main()

    @staticmethod
    def inject_game_state(state: GameState) -> bool:
        """Function to inject GameState object into DPG data register.

        Args:
            state (GameState): GameState object to be injected.

        Raises:
            Exception: If it wasn't able to inject the data.

        Returns:
            bool: True if successful, False otherwise
        """

        try:
            core.log_debug("Enter GUI.inject_game_state")
            core.log_debug(state)
            core.add_data("__active_state", state)
            return True
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def consume_game_state(sender, data):
        """This function interprets the game state and builds the GUI accordingly"""

        # Notify of code execution
        print(f"DEBUG | Entering func: `GUI.Commands.consume_game_state`")

        # Get game state from data store
        gs = core.get_data("__active_state")

        # And add some of that information to the GUI, to prove the concept.
        core.add_text(f"{gs.state.name = }", parent="Main")
        core.add_text("Okay, so I consumed the game state.", parent="Main")

    def grant_cmds(self, _beacon: RPSBeacon):
        """Dynamically generate callbacks as static methods, injecting beacon functions.

            This function declares _Commands, and pushes this command's `self` 
            into the definition scope anywhere we need to inject a dependency. 

        Args:
            beacon: An active RPSBeacon object, to be injected in below static methods.
        """

        class _Commands:
            """Callbacks to be bound to DPG elements and Beacon signals."""

            # grab the GUI instance from enclosing scope
            nonlocal _beacon

            @staticmethod
            def request_game_state(sender, data):
                """GUI method for requesting game state through a Beacon"""
                nonlocal _beacon
                print(f"DEBUG | Entering func: `GUI.commands.request_game_state`")
                print(f"DEBUG | {_beacon = }")

                # Get our dummy User instance, because the API requires a User for auth.
                user = core.get_data("user")

                # Construct data dict to pass the User and Callable to async func
                data = {"user": user, "__injector": GUI.inject_game_state}

                # This is where it's broken.
                print(
                    f"DEBUG | NOTE:",
                    f"The async function `beacon.get_game_state`",
                    f"should immediately follow.",
                )
                core.run_async_function(
                    _beacon.get_game_state,
                    data,
                    return_handler=GUI.consume_game_state,
                )

        self.commands = Commands

    def main(self):
        with simple.window("Main"):
            core.show_logger()
            core.add_text("Hello World!")
        core.set_primary_window("Main", True)
        core.add_button(
            "Request GameState",
            parent="Main",
            callback=self.commands.request_game_state,
            callback_data="mock data" + "moremockdata",
        )

    @staticmethod
    def welcome_screen():
        core.add_text("It's-a me: the welcome screen!")

    @staticmethod
    def requesting_lobby():
        core.add_text("And welcome to the Lobby for the Lobby!")

    def start_gui(self):
        """Simple method to set the primary window and execute lift-off"""
        core.set_primary_window("Main", True)
        core.enable_docking()
        core.start_dearpygui()
