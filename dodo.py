import os
import sys


def task_makedocs():
    cmd_str = "pdoc3 --html --output-dir docs src --force"
    return {
        "actions": [(cmd_str)],
        "params": [
            {
                "name": "force",
                "short": "f",
                "long": "force",
                "type": bool,
                "default": False,
            }
        ],
        "verbosity": 2,
    }


def task_start_server():
    def _cd(flag):
        print(f"{flag = }")
        return os.chdir(os.path.join(sys.path[0], "src"))

    def _start(flag):
        print(f"{flag = }")
        return os.system(f"uvicorn {'--reload' if flag else ''} server:app")

    return {
        "params": [
            {
                "name": "reload",
                "short": "r",
                "long": "reload",
                "default": False,
                "help": "Ask `uvicorn` to reload the server after code changes",
            }
        ],
        "actions": [((_cd(False),), (_start(True),))],
        "verbosity": 2,
    }