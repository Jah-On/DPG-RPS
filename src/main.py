"""This is the main jumping off point for GUI and CLI interfaces.

This file will contain the logic that says "Okay, this is being launched without
command line arguments, so the GUI Launcher needs to be loaded. Or, if there ARE
arguments present, then it can start and/or configure the server.
"""
# from server import server
from .client import client
from .launcher import launcher


def launch_launcher():
    launcher.main(client)


def cli():
    """Server init commands go here"""
    ...


if __name__ == "__main__":
    launch_launcher()
