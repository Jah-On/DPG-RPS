from .tui import TUI
from client.client import RPSBeacon


def main():
    # Light the beacon
    beacon = RPSBeacon()

    # Construct our GUI, injecting the beacon.
    g = TUI(beacon)

    # All the magic happens on init, so just start the GUI.
    # g.main()