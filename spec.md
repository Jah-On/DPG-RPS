# DPG-RPS Specification

## ***Components***

1. Launcher 

    ***Description***
    * This app is meant to facilitate initiating the game experience.
    * Because DPG-RPS comes as a bundle, the Launcher will serve as the single interface for both Client and Server.

    ***Utilizes***
    * server.authenticate()
    * server.register_new_user()
    * server.request_connection()
    * server.request_available_players()
    * server.request_connection_with_player()

    ***API Functions***
    * none

    ***Internal Functions***
    * // TODO

1. Client

    ***Description***
    * While the Server is naturally the brain, and the Launcher is the GUI, what space does that leave for the Client?
    * The Client does not have a very glamorous job. In essence, it serves as the translator and messenger for instructions from the Brain to the Body. 
    * The Client is GUI-agnostic. The objective is to expose an API that could be consumed by ANY framework, and to separate two major concerns: 
        * Coordinating the flow of the game
        * Providing an interface for the game

    ***Utilizes***
    * server.submit_move(Move)

    ***API Functions***
    * // TODO

    ***Internal Functions***
    * listen_for_command(Server)
    * command_interpreter(Command)
    * consume_game_state()


1. Server

    ***Description***
    * Okay, big brain time. 
    * Regardless of where the ball was hit from, this is where the game is "played".
    * What I mean is that it's the Server's job to guarantee that the game state is consistent across Clients. 
    * Your move will be submitted to the Server, and the Server will tell you what happened. 
    * The Server will never ask the Client to make an assumption about game state, or ask it to infer a result, or to perform a calculation.


    ***Utilizes***
    * none

    ***API Functions***
    * register_new_user()
    * authenticate()
    * request_connection()
    * request_available_players()
    * request_connection_with_player()

    ***Internal Functions***
    * // TODO

    ***Attributes***
    * lobby: List(User)
    * active_game_sessions: List(Game)
    * active_connections: List(Connection)
---


## ***Class Specification***

```
class Snowflake(ABC):
    """Base class for all game objects.

    Attributes:
        id (int): Unique ID for object
    

    """
    ...
```

```
class Connection(Snowflake):
    """Object for management of socket connection

    Attributes:
        id (int): Unique ID for object
        socket (Socket)
        user (User)

    Functions:
        send_data(data)        # Really necessary?
        send_command(Command)  # Really necessary?


    """
```

```
class Command(ABC, Snowflake, GameState):
    """ An instruction packet, sent one way only—from Server to Client.
    
    Contains instructions that trigger state changes in the UI.
    Should always be subclassed, with more specific information made available
    for each type of Command (display_game_over, await_response, )

    Attributes:
        id (int): Unique ID for object
        game_state (GameState): Most up-to-date game state information available. Every Command will provide the most current game state with every request for information that would change it. 


    
    Functions:
        execute()
            * contains the functions necessary to trigger change in the client

    """
```
// TODO: Implement below list of commands as subclasses.

```
Command List:
* prompt_move
* display_result
* wait_for_result
* prompt_new_game
```


```
class Game(Snowflake):
    """A class for housing game logic and managing the game's internal state.

    Attributes:
        id (int): Unique ID for object
        current_state
        move_history
        players_in_game

    Functions:
        get_game_state()
            * return a serializable, file writable, importable save state.
        load_game_state(state_file)
            * restores internal game state from file.
        submit_move(move)

    """
```


```
class User(Snowflake):
    """An object with basic user information.

    Attributes:
        id (int): Unique ID for object
        name (str): The user's display name

    """
```


```
class Move(Snowflake):
    """An object containing information about the move and the user

    Attributes:
        id (int): Unique ID for object
        move (str): either "rock", "paper", or "scissors"
        user (User): the `User` submitting the move
    
    """
```




---

```
def func(var_name: type) -> bool:
    """ Docstring text

    Arguments:
        var_name: [description]

    Returns:
        bool: [description]

    Raises:
        ExceptionType: [description]

    """
    ...
```