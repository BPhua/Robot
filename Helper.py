import Errors

def parseCommand(command: str) -> list:
    if command == "STOP":
        raise Errors.ProgramTerminatedByUser

    command = command.split(" ")
    # Checking for valid input characters
    for input in command:
        if len(input) == 0:
            raise Errors.NoMovementCommandError
        if input not in (['N', 'S', 'E', 'W']):
            raise Errors.InvalidMovementCommandError
    return command


def validateRobotStartingPosition(startX, startY, grid) -> None:
    if startX not in range(grid.getLower(), grid.getUpper() + 1) or startY not in range(grid.getLower(), grid.getUpper() + 1):
        raise Errors.InvalidStartingPositionError