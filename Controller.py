from Robot import Robot
from Grid import Grid
import Errors

class Controller:

    def __init__(self, input: list, robot: Robot, grid: Grid):
        self.input = input
        self.robot = robot
        self.grid = grid

    def start(self) -> None:
        for command in self.input:
            self.move(command)

    def move(self, command: str) -> None:
        if command == 'N':
            next = self.robot.getY() + 1
            if next <= self.grid.getUpper():
                self.robot.updateY(next)
            else:
                self.outOfBoundsHandler(command)
        elif command == 'S':
            next = self.robot.getY() - 1
            if next >= self.grid.getLower():
                self.robot.updateY(next)
            else:
                self.outOfBoundsHandler(command)
        elif command == 'E':
            next = self.robot.getX() + 1
            if next <= self.grid.getUpper():
                self.robot.updateX(next)
            else:
                self.outOfBoundsHandler(command)
        elif command == 'W':
            next = self.robot.getX() - 1
            if next >= self.grid.getLower():
                self.robot.updateX(next)
            else:
                self.outOfBoundsHandler(command)

        print(f"INFO - Moving {command} ... New position at ({self.robot.getX()}, {self.robot.getY()})")

    def outOfBoundsHandler(self, command: str) -> None:
        raise Errors.OutOfBoundsError(command)