class GameException(Exception):
    pass

class InputLatencyException(GameException):
    def __init__(self, message="Input latency too high."):
        self.message = message
        super().__init__(self.message)

class ConnectionTimeoutException(GameException):
    def __init__(self, message="Connection timed out."):
        self.message = message
        super().__init__(self.message)

class InvalidInputException(GameException):
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)

class UnsupportedGameModeException(GameException):
    def __init__(self, mode, message="Unsupported game mode."):
        self.mode = mode
        self.message = f"{message} Mode: {mode}"
        super().__init__(self.message)