from .gui import GUI


def main(client):
    # Instantiate our GUI, and pass it a Commander.
    g = GUI(client)

    g.main()

    g.start_gui()