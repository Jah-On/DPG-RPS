"""Module for building a TUI for Rock Paper Scissors."""

from typing import Callable
from coverage import control

from prompt_toolkit import PromptSession, prompt
from prompt_toolkit import print_formatted_text as print
from prompt_toolkit.application.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import (
    Float,
    FloatContainer,
    Container,
    VSplit,
    HSplit,
    Window,
)
from prompt_toolkit.layout.controls import (
    BufferControl,
    FormattedTextControl,
    UIControl,
)
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.formatted_text.base import FormattedText
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts.dialogs import input_dialog
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Frame

from client.client import RPSBeacon
from obj.objects import GameState, User, States
from obj.objects import Mocks

m_user = Mocks.utils.make_mock_User(Mocks.users["user1"])


# 1. The layout
left_text = HTML("<reverse>transparent=False</reverse>\n")
right_text = HTML("<reverse>transparent=True</reverse>")
quit_text = "Press ESCAPE DELETE to quit."


class TUI:
    def plank(
        self,
        left: UIControl,
        top: UIControl,
        bottom: UIControl,
    ) -> Container:
        """The primary drawing surface for this app."""
        ctr = VSplit(
            [Window(content=left)],
            HSplit(
                [
                    Window(content=top),
                    Window(content=bottom),
                ]
            ),
        )
        return ctr

    def gs_control(self, gs_ft: FormattedText) -> FormattedTextControl:
        _style = Style(
            [
                ("game_id", "ansigreen"),
                ("state", ""),
                ("players", ""),
                ("ready", ""),
                ("current_moves", ""),
                ("moves_history", ""),
                ("winner", ""),
            ]
        )
        return FormattedTextControl(
            text=gs_ft, style="class:game_id black-on-white, class:state ansigreen"
        )

    def empty_control(self) -> UIControl:
        return FormattedTextControl(text="")

    def _build_keybindings(self, kb: KeyBindings) -> KeyBindings:
        @kb.add("escape", "delete")
        def exit_(event):
            """Pressing ESC DEL will exit the user interface."""
            event.app.exit()

        return kb

    def _consume_game_state(self, gs: GameState) -> None:
        """Directly apply game state to UI"""
        return None

    def _gs_to_FT(self, gs: GameState) -> FormattedText:
        """Helper to convert game state to a FormattedText object"""

        text = FormattedText(
            [
                ("class:game_id", str(gs.game_id)),
                ("class:state", str(gs.state)),
                ("class:players", str(gs.players)),
                ("class:ready", str(gs.ready)),
                ("class:current_moves", str(gs.current_moves)),
                ("class:moves_history", str(gs.moves_history)),
                ("class:winner", str(gs.winner)),
            ]
        )
        return text

    def __init__(self, beacon: RPSBeacon):
        # Save our beacon
        self.beacon = beacon

        # Define a FormattedText object for the game state
        self._game_state = beacon.get_game_state(m_user)
        gsFT = self._gs_to_FT(self._game_state)

        # Create a keybinding object, and pass it to a helper function to decorate.
        kb = KeyBindings()
        kb = self._build_keybindings(kb)

        gs_pane = self.gs_control(gsFT)
        empty = self.empty_control()
        hard_plank = self.plank(left=empty, top=gs_pane, bottom=empty)

        # Instantiate an app, provide our layout & keybindings, and make it full-screen
        self.app = Application(
            layout=Layout(hard_plank),
            key_bindings=kb,
            mouse_support=True,
            full_screen=True,
        )

        # And TUI we have liftoff...
        self.app.run()

    def welcome(self):
        message_dialog(
            title="Welcome",
            text="Press ENTER to continue.",
        ).run()

    def login(self):
        username = input_dialog(
            title="Sign In",
            text="Username:",
        ).run()
        password = input_dialog(
            title="Sign In",
            text="Password:",
            password=True,
        ).run()

    def print_banner(self):
        """Serving as placeholder text-only Welcome screen"""
        text = FormattedText(
            [
                ("class:header", "Welcome to TUI-RPS!"),
                ("", "\n"),
                ("class:sub", "Because DPG just wasn't working out."),
            ]
        )
        style = Style.from_dict(
            {
                "header": "ansigreen",
                "sub": "ansiblue",
            }
        )
        print(text, style=style)

    # region abstract methods
    @staticmethod
    def inject_game_state(state: GameState) -> bool:
        """Function to inject GameState object into GUI's data register.

        Args:
            state (GameState): GameState object to be injected.

        Raises:
            Exception: If it wasn't able to inject the data.

        Returns:
            bool: True if successful, False otherwise
        """
        return False

    @staticmethod
    def consume_game_state(sender, data):
        """This function interprets the game state and builds the GUI accordingly"""
        pass

    def generate_commands(self):
        """Dynamically generate callbacks as static methods, injecting beacon functions.

        Args:
            beacon: An active RPSBeacon object, to be injected new static methods.
        """

        class Commands:
            """Callbacks to be bound to DPG elements and Beacon signals."""

            pass

    @staticmethod
    def welcome_screen():
        raise NotImplementedError

    @staticmethod
    def requesting_lobby():
        raise NotImplementedError

    def start_gui(self):
        raise NotImplementedError

    # endregion
