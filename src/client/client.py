class Client:
    @staticmethod
    def listen_for_command(var_name: type) -> bool:
        """Wait for a Command object from server.

        Arguments:
            var_name (type): [description]

        Returns:
            bool: [description]

        Raises:
            ExceptionType: [description]

        """
        ...

    @staticmethod
    def submit_move():
        pass

    @staticmethod
    async def get_game_state():
        pass