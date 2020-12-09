from .gui import GUI
from client import RPSBeacon


def main():
    # Light the beacon
    beacon = RPSBeacon()

    # Make a GUI instance, injecting the beacon.
    g = GUI(beacon)

    # Wow, actually, let's *triple* check that our dependencies injected.
    g.commands._verify(caller="launcher.__init__:main")

    # Pick out the main interface.
    g.main()

    # And liftoff.
    g.start_gui()