import dearpygui.core as core
import dearpygui.simple as simple


class GUI:
    def __init__(self, client):
        self.client = client

    def main(self):
        ...

    def _consume_game_state(self, state):
        ...

    def render_loop(self):
        ...

    def clear_screen(self):
        pass

    def welcome_screen(self):
        core.add_text("Welcome to DPG-RPS!", parent="Main")

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
        with simple.window("DPG-RPS", menubar=True):
            ...
        core.start_dearpygui(primary_window="DPG-RPS")