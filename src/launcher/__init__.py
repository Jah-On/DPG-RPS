from .gui import GUI
from client import RPSBeacon


def main():
    # Light the beacon
    beacon = RPSBeacon()

    # Construct our GUI, injecting the beacon.
    g = GUI(beacon)

    # All the magic happens on init, so just start the GUI.
    g.start_gui()