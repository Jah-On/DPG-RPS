import dearpygui.core as core
import dearpygui.simple as simple
from rich import traceback

traceback.install()


def main():
    with simple.window("Main Window"):
        core.add_text("Hello World!")

    core.start_dearpygui()


if __name__ == "__main__":
    main()