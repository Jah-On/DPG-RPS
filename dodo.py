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
