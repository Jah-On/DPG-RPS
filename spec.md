# API Specifications

## ***Components***

1. Launcher 

    ***Utilizes***
    * server.request_connection()
    * server.request_available_players()
    * server.request_connection_with_player

    ***API Functions***
    * none

    ***Internal Functions***
    * // TODO

1. Client

    ***Utilizes***
    * server.submit_move()

    ***API Functions***
    * // TODO

    ***Internal Functions***
    * listen_for_command(Server)
    * command_interpreter(Command)


1. Server

    ***Utilizes***
    * none

    ***API Functions***
    * request_connection()
    * request_available_players()
    * request_connection_with_player()

    ***Internal Functions***
    * // TODO

---

## ***API***
### Launcher



### Client

```
def listen_for_command(var_name: type) -> bool:
    """ Wait for a Command

    Arguments:
        var_name (type): [description]

    Returns:
        bool: [description]

    Raises:
        ExceptionType: [description]

    """
    ...
```




### Server

```
def submit_move(var_name: type) -> bool:
    """ Docstring text

    Arguments:
        arg1 (NamedTuple): [description]

    Returns:
        True if successful, False otherwise

    Raises:
        ExceptionType: [description]
    """

    ...
```

* def request_connection(user_identifier_object)
* def request_available_players()
  * gets a list of players in the server lobby, in order to request an opponent
  * returns a list of User snowflakes
* def request_connection_with_player
  * a request meant for telling the server which player you want to connect with. 

---

## ***Class Specification***

```
class Snowflake(ABCBaseClass):
    """Base class for all API objects.

    Attributes:
        id (int): Unique ID for object
    

    """
    ...
```


```
class Command(Snowflake):
    """ An instruction packet, received by client from server.
    
    Contains instructions that trigger state changes in the UI.


    """
```

```
class GameState(Snowflake):
    """
        Attributes:
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
    """

    Attributes:
        name (str): The user's display name
        current_game 

    """
```






---

```
def func(var_name: type) -> bool:
    """ Docstring text

    Argumentss:
        var_name: [description]

    Returns:
        bool: [description]

    Raises:
        ExceptionType: [description]

    """
    ...
```