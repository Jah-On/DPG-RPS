# help/async debugging

It's a Rock, Paper, Scissors game, played over the web, via FastAPI requests.

Okay.

So.

I'm trying to post an HTTP Request & load the response into DPG's data register.

One Button. One Command. And who knows how many callbacks.

The RPSBeacon class sits in as a Commander object in this scenario, and
it serves as the communication layer between GUI and the Server.

Because the Server is using FastAPI, the communications are request-and-response
based. The Client submits information to the Server, the Server will do calculations
about the game state, and then will return the updated game state, with a set of
instructions about what to do next.

In essence, the Server will always provide enough information about the game state for
any client to be able to rebuild it from scratch. The GUI only needs an instance of the
GameState class in order to be in-sync with the Server and every other Client.

But because these requests may take a while to return (if you've submitted your move,
but your opponent has not yet, for example), so I want to run them asynchronously,
and then trigger the GUI to refresh once the response is processed.

In this way, the GUI essentially become a "state consuming machine". There is no game
logic defined in the GUI.

```
So:
    Main.py calls the Launcher.
        Launcher makes an RPSBeacon, passing it to the GUI, then starts the GUI.
        The GUI loads the RPSBeacon into the data store.
            Then it creates a window, line of text, and a button
            The button will run a callback to request the game data.
                This travels through:
                    GUI.commands.request_game_data()
                    core.run_async_function()
                        RPSBeacon.get_game_state()
                        RPSBeacon._mock_request()
                and finally be stored by RPSBeacon via GUI.inject_game_state().

            When the server responds, the GUI will add a string to the window that says
            "It changed!" instead of the default "fake"
```
See Install and Run sections below.


# DPG-RPS
## *Rock, Paper, Sockets!*


### Prequisites
* `poetry`


### Install
1. `git clone https://github.com/Jah-On/DPG-RPS.git`
1. `cd DPG-RPS/`
1. `git checkout help/async`
1. `poetry install`

### Start Server
1. `poetry run doit start_server

### Run Client
1. `poetry run python src/main.py`
