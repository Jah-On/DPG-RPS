"""Module for building a TUI for Rock Paper Scissors."""

from typing import Callable

from prompt_toolkit import PromptSession, prompt
from prompt_toolkit import print_formatted_text as print
from prompt_toolkit.application.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import (
    Float,
    FloatContainer,
    VSplit,
    HSplit,
    Window,
)
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.formatted_text.base import FormattedText
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts.dialogs import input_dialog
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Frame

from client.client import RPSBeacon
from obj.game_objects import GameState, User, States
from obj.game_objects import Mocks

m_user = Mocks.utils.make_mock_GameState(Mocks.mocks.users["user1"])

LIPSUM = " ".join(
    (
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Maecenas quis interdum enim. Nam viverra, mauris et blandit malesuada, ante est
bibendum mauris, ac dignissim dui tellus quis ligula. Aenean condimentum leo at
dignissim placerat. In vel dictum ex, vulputate accumsan mi. Donec ut quam
placerat massa tempor elementum. Sed tristique mauris ac suscipit euismod. Ut
tempus vehicula augue non venenatis. Mauris aliquam velit turpis, nec congue
risus aliquam sit amet. Pellentesque blandit scelerisque felis, faucibus
consequat ante. Curabitur tempor tortor a imperdiet tincidunt. Nam sed justo
sit amet odio bibendum congue. Quisque varius ligula nec ligula gravida, sed
convallis augue faucibus. Nunc ornare pharetra bibendum. Praesent blandit ex
quis sodales maximus. """
        * 100
    ).split()
)


# 1. The layout
left_text = HTML("<reverse>transparent=False</reverse>\n")
right_text = HTML("<reverse>transparent=True</reverse>")
quit_text = "Press ESCAPE DELETE to quit."


class TUI:
    def _build_keybindings(self, kb: KeyBindings) -> KeyBindings:
        @kb.add("escape", "delete")
        def exit_(event):
            """
            Pressing Ctrl-Q will exit the user interface.

            Setting a return value means: quit the event loop that drives the user
            interface and return this value from the `Application.run()` call.
            """
            event.app.exit()

        return kb

    def __init__(self, beacon: RPSBeacon):
        # Save our beacon
        self.beacon = beacon

        # region Define layout

        buffer1 = Buffer()

        root_ctr = VSplit(
            [
                # One window that holds the BufferControl with the default buffer on
                # the left.
                Window(content=BufferControl(buffer=buffer1)),
                # A vertical line in the middle. We explicitly specify the width, to
                # make sure that the layout engine will not try to divide the whole
                # width by three for all these windows. The window will simply fill its
                # content by repeating this character.
                Window(width=1, char="|"),
                # Display the text 'Hello world' on the right.
                Window(content=FormattedTextControl(text="Hello world")),
            ]
        )

        body = FloatContainer(
            content=Window(FormattedTextControl(LIPSUM), wrap_lines=True),
            floats=[
                # Important note: Wrapping the floating objects in a 'Frame' is
                #                 only required for drawing the border around the
                #                 floating text. We do it here to make the layout more
                #                 obvious.
                # Left float.
                Float(
                    Frame(Window(FormattedTextControl(left_text), width=20, height=4)),
                    transparent=False,
                    left=0,
                ),
                # Right float.
                Float(
                    Frame(Window(FormattedTextControl(right_text), width=20, height=4)),
                    transparent=True,
                    right=0,
                ),
                # Quit text.
                Float(
                    Frame(
                        Window(FormattedTextControl(quit_text), width=18, height=1),
                        style="bg:#ff44ff #ffffff",
                    ),
                    top=1,
                ),
            ],
        )

        # endregion

        # Create a keybinding object, and pass it to a helper function to decorate.
        kb = KeyBindings()
        kb = self._build_keybindings(kb)

        # Instantiate an app, provide our layout & keybindings, and make it full-screen
        self.app = Application(
            layout=Layout(body),
            key_bindings=kb,
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
