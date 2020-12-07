"""This is the main jumping off point for GUI and CLI interfaces.

This file will contain the logic that says "Okay, this is being launched without
command line arguments, so the GUI Launcher needs to be loaded. Or, if there ARE
arguments present, then it can start and/or configure the server.
"""
# built-ins
import asyncio

# libraries
import pretty_errors

# # This app's resources
# from server import server
# from client import client
from launcher import launcher


async def launch_launcher():
    await launcher.main()


def cli():
    """Server init commands go here"""
    ...


if __name__ == "__main__":
    asyncio.run(launch_launcher())


"""
Submit & Get:

One Command. 

Submit a request to the server. Display the information it returns.

Main calls the launcher.
    The Launcher makes a Client, and a GUI.
    The GUI creates a window, a button, and a line of text.
        The button will submit a request to the server.
        When the server responds, the GUI will add a string to the window.
    The Client will expose one command: Commands.submit_generic().
        When the request is received, then a new method will be triggered
            This will print the string to the window.
        The tricky bit is: how does the client pass information back to the GUI?

"""