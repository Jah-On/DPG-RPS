"""This is the main jumping off point for GUI and CLI interfaces.

This file will contain the logic that says "Okay, this is being launched without
command line arguments, so the GUI Launcher needs to be loaded. Or, if there ARE
arguments present, then it can start and/or configure the server.
"""
# built-ins


# libraries
import pretty_errors  # Pretty tracebacks, no config necessary

# # This app's resources
# from server import server
# from client import client
from launcher import launcher


def launch_launcher():
    launcher.main()


if __name__ == "__main__":
    launch_launcher()


"""
Okay.

Submit an API call & load the response into DPG's data register.

One Button. One Command. Who knows how many callbacks.

The RPSBeacon class sits in as a Commander object in this scenario, and
it serves as the communication layer between GUI and the Server.

Because the Server is using FastAPI, the communications are request-and-response
based. The Client submits information to the Server, the Server will do calculations
about the game state, and then will return the updated game state, with a set of
instructions about what to do next.

In essence, the Server will always provide enough information about the game state for
any client to be able to rebuild it from scratch. The GUI only needs an instance of the
GameState class in order to be in-sync with the Server and every other Client.

But because these requests may take a while to return (if you've submitted your move,
but your opponent has not yet, for example), so I want to run them asynchronously,
and then trigger the GUI to refresh once the response is processed.

In this way, the GUI essentially become a "state consuming machine". There is no game
logic defined in the GUI.

So:
    Main.py calls the Launcher.
        Launcher makes an RPSBeacon, passing it to the GUI, then starts the GUI.
        The GUI loads the RPSBeacon into the data store.
            Then it creates a window, line of text, and a button
            The button will run a callback to request the game data.
                This travels through:
                    GUI.commands.request_game_data()
                    core.run_async_function()
                        RPSBeacon.get_game_state()
                        RPSBeacon._mock_request()
                and finally be stored by RPSBeacon via GUI.inject_game_state().

            When the server responds, the GUI will add a string to the window that says
            "It changed!" instead of the default "fake"


"""
