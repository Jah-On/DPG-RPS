from typing import NamedTuple
import dearpygui.core as core
import dearpygui.simple as simple

# from rich import traceback

# traceback.install()


def main():
    with simple.window("Main Window"):
        core.add_text("Hello World!")

    core.start_dearpygui()


if __name__ == "__main__":
    main()


def func(arg1: NamedTuple) -> bool:
    """

    Args:
        arg1 (NamedTuple): [description]

    Returns:
        bool: [description]
    """
    ...


class Command:
    """[summary]"""

    def __init__(self, request):
        self.__request = request
        ...

    @property
    def request(self):
        return self.__request

    ...