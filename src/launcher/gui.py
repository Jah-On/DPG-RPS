from typing import Callable
import dearpygui.core as core
import dearpygui.simple as simple
from obj import IClientCommander, IGUI
from obj.game_objects import GameState


class GUI(IClientCommander):
    class Commands(IGUI):
        """Commands exposed to the Client instance"""

        def __init__(self, ClientCommands):
            """I can bind Client commands to GUI commands here"""
            ...

        @staticmethod
        def inject_game_state(state: GameState):
            core.add_data("__active.state", state)

        @staticmethod
        def consume_game_state():
            """This function interprets the game state and builds the GUI accordingly"""
            state = core.get_data("__active.state")

            if state.state == "Welcome":
                GUI.welcome_screen()

    class DPGCallbacks:
        """A container for all the callback consumed by DPG.

        These must be declared as static methods."""

        @staticmethod
        def start_game(sender, data):
            core.run_async_function(
                GUI.start_game,
                None,
                return_handler=GUI.Commands.consume_game_state,
            )
            pass

    def __init__(self, client):
        # Create a new Iinstance of our Client's commands, to be consumed by THIS GUI's instance.
        self.commands: IClientCommander = client().Commands
        self.cb = GUI.DPGCallbacks
        self.commands.get_game_state_to_target(self.Commands.inject_game_state)
        self.main()

    def submit_move(self, move):
        pass

    def get_game_state_to_target(self, target: Callable) -> None:
        pass

    def request_start_game(self):
        pass

    def start_game(self):
        self.commands.start_game()

    def main(self):
        with simple.window("Main"):
            core.add_text("Hello World!")
        core.set_primary_window("Main", True)
        self.Commands.consume_game_state()

    def _consume_game_state(self, state):
        ...

    @staticmethod
    def welcome_screen():
        core.add_text("Welcome to DPG-RPS This is the Welcome screen!", parent="Main")
        core.add_button("Start Game", callback=self.cb.start_game)

    def start_gui(self):
        """Simple method for exposing the GUI lift-off command"""
        core.start_dearpygui()
