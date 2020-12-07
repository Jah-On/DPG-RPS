from .gui import GUI
from client.client import RPSBeacon


async def main():
    # Construct our GUI, attaching it to an ICommander object.
    g = await GUI(RPSBeacon)

    # Everything happens in the constructor, so just start the GUI.
    g.start_gui()