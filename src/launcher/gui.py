import dearpygui.core as core
import dearpygui.simple as simple
from obj import IGUI
from obj.game_objects import GameState


class GUI:
    class Commands(IGUI):
        @staticmethod
        def inject_game_state(state: GameState):
            core.add_data("__active.state", state)

        @staticmethod
        def consume_game_state():
            """This function interprets the game state and builds the GUI accordingly"""
            state: GameState
            state = core.get_data("__active.state")

            if state.state == "Welcome":
                GUI.welcome_screen()

    def __init__(self, client):
        # Create a new INSTANCE, of our client, to be consumed by THIS GUI's instance.
        self.client = client()
        self.client.get_game_state_to_target(self.Commands.inject_game_state)
        self.main()

    def main(self):
        with simple.window("Main"):
            core.add_text("Hello World!")
        core.set_primary_window("Main", True)
        self.Commands.consume_game_state()

    def _consume_game_state(self, state):
        ...

    def render_loop(self):
        ...

    def clear_screen(self):
        pass

    def welcome_screen(self):
        core.add_text("Welcome to DPG-RPS This is the Welcome screen!", parent="Main")

    def game_screen(self):
        pass

    def get_move(self, sender, data):
        pass

    def get_move_screen(self):
        core.add_combo(
            "Move Select",
            items=["Rock", "Paper", "Scissors"],
            callback=self.client.submit_move,
            parent="Main Window",
        )

    def start_gui(self):
        """Simple method for exposing the GUI lift-off command"""
        core.start_dearpygui()
