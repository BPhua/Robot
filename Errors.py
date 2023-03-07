class InvalidMovementCommandError(Exception):
    def __str__(self):
        return "ERROR - Invalid movement command entered. Please enter one of N, S, E, W separated by whitespace. Try again."
    pass

class NoMovementCommandError(Exception):
    def __str__(self):
        return "ERROR - No movement command entered. Try again."
    pass

class InvalidStartingPositionError(Exception):
    def __str__(self):
        return "ERROR - Invalid starting position. Try again."
    pass

class ProgramTerminatedByUser(Exception):
    def __str__(self):
        return "INFO - Program Exiting ..."
    pass

class OutOfBoundsError(Exception):
    def __init__(self, command):
        self.command = command
    def __str__(self):
        return f"ERROR - Moving {self.command} ... Robot will go out of bounds."
    pass