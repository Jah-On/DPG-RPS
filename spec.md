# API Specifications

## ***Components***

1. Launcher 

    ***Utilizes***
    * server.authenticate()
    * server.register_new_user()
    * server.request_connection()
    * server.request_available_players()
    * server.request_connection_with_player

    ***API Functions***
    * none

    ***Internal Functions***
    * // TODO

1. Client

    ***Utilizes***
    * server.submit_move(Move)

    ***API Functions***
    * // TODO

    ***Internal Functions***
    * listen_for_command(Server)
    * command_interpreter(Command)


1. Server

    ***Utilizes***
    * none

    ***API Functions***
    * authenticate
    * request_connection()
    * request_available_players()
    * request_connection_with_player()
    * register_new_user()

    ***Internal Functions***
    * // TODO

    ***Attributes***
    * lobby: List(User)
    * active_game_sessions: List(Game)
    * active_connections: List(Connection)
---

## ***API***
### Launcher

```
// TODO
```

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

* def authenticate(user, pass):
  * Returns a NamedTuple of format (`Server`, `User`) if successful.
  * Raises AuthenticationError if unsuccessful
* def register_new_user(user, pass):
    * Returns True if successful
    * Raises RegistrationError otherwise
* def request_connection(user_identifier_object):
* def request_available_players():
  * gets a list of players in the server lobby, in order to request an opponent
  * returns a list of User snowflakes
* def request_connection_with_player:
  * a request meant for telling the server which player you want to connect with. 

---

## ***Class Specifications***

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
class Command(ABC, Snowflake):
    """ An instruction packet, received by client from server.
    
    Contains instructions that trigger state changes in the UI.
    Should always be subclassed, with more specific information made available
    for each type of Command (display_game_over, await_response, )

    Attributes:
        id (int): Unique ID for object

    
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