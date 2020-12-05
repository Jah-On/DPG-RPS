from .gui import GUI


def main(client):
    # Construct our GUI, attaching it to an ICommander object.
    g = GUI(client)

    # Everything happens in the constructor, so just start the GUI.
    g.start_gui()