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

        # Register the beacon's `this_user` identifier with data store
        core.add_data("_this_user", self.beacon.this_user)

        # Let's add a mock GameState to the register, too.
        core.add_data("__active_state", Mocks.make_gs("welcome"))

        # Dynamically generate static methods to be used as callbacks
        # This grants our Beacon instance a .commands namespace on init.
        self.grant_cmds(beacon)

        # Just double check that our dependency injection hack worked:
        self.commands._verify(caller="launcher.gui.GUI:__init__")

    @staticmethod
    def inject_gs(state: GameState) -> None:
        """Function to inject GameState object into DPG data register.

        Args:
            state (GameState): GameState object to be injected.
        """

        core.add_data("__active_state", state)

    @staticmethod
    def consume_game_state(sender, data):
        """This function interprets the game state and builds the GUI accordingly"""

        # Get game state from data store
        gs: GameState = core.get_data("__active_state")

        # Programmatically unpack GameState fields into DPG data store.
        for attr in gs:
            _0 = attr[0]
            _1 = attr[1]
            core.add_text(f"Adding '_{_0}' as {_1}", parent="Main")
            core.add_value(f"_{_0}", _1)
            core.add_text(name="bad_name", source=f"_{_0}", parent="Game State")

        # And add some of that information to the GUI, to prove the concept.
        core.add_text(f"{gs.state.name = }", parent="Main")
        core.add_text("Okay, I consumed the game state.", parent="Main")

    def grant_cmds(self, _beacon: RPSBeacon):
        """Dynamically generate callbacks as static methods, injecting beacon functions.

            This function declares _Commands, and pushes this command's `_beacon`
            parameter into the definition scope anywhere we need to inject a `Client`
            function

        Args:
            beacon: An active RPSBeacon object, to be injected in below static methods.
        """

        class _Commands:
            """Callbacks to be bound to DPG elements and Beacon signals."""

            # grab the GUI instance from enclosing scope
            nonlocal _beacon

            @staticmethod
            def _verify(caller: str):
                """Helper to test that _Commands instance was created."""
                core.log_debug(f"_Commands attached to {caller}")

            @staticmethod
            def request_game_state(sender, data):
                """GUI callback for requesting game state through a Beacon"""
                nonlocal _beacon

                # Get our dummy User instance, because the API requires a User for auth.
                user = core.get_data("_this_user")

                # Construct data dict to pass the User and Callable to async func
                data = {"user": user, "__injector": GUI.inject_gs}

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

        self.commands = _Commands

    def main(self):
        core.add_window("Main")
        core.end()

        GUI._mod_game_state()

        core.add_window("Current User")
        core.end()

        core.add_window("Opponent")
        core.end()

        core.add_window("Game Prompt")
        core.end()

        core.add_window("Move Select")
        core.end()

        core.add_text("GameState stuff", parent="Game State")

        core.set_primary_window("Main", True)
        core.add_button(
            "Request GameState",
            parent="Main",
            callback=self.commands.request_game_state,
            callback_data="mock data" + "moremockdata",
        )
        core.add_text("State", source="_state", parent="Game State")

    @staticmethod
    def _mod_game_state():
        with simple.window("Game State"):
            core.add_text("This is the Game State module.")
            core.add_table("Game State", ["property", "value"])
            gs: GameState = core.get_data("__active_state")
            for i, attr in zip(range(0, 7), gs):
                print(i)
                core.add_row("Game State", [attr[0], attr[1]])

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
