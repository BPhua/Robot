from Robot import Robot
from Grid import Grid
from Controller import Controller
import Errors
import Helper

def main(): 

    print("INFO - Program Starting...")

    # Initialise Grid object to store attributes of building
    grid = Grid(0, 9)
    print("INFO - Grid of size 10x10 initialised with southwest corner represented by (0, 0). \n")


    # Ask user for robot's starting position
    while True:
        startX = int(input("Enter robot's starting X position: "))
        startY = int(input("Enter robot's starting Y position: "))
        try:
            Helper.validateRobotStartingPosition(startX, startY, grid)
            break
        except Errors.InvalidStartingPositionError as err:
            print(err)
            continue

    # Initialise Robot with starting position
    robot = Robot(startX, startY)

    # Ask user for commands
    while True:
        try:
            command = input("Enter movement commands separated by whitespace, or STOP to exit: ")
            # Parse input sequence separated by whitespace
            inputSequence = Helper.parseCommand(command)
        except Errors.NoMovementCommandError as err:
            print(err)
            continue
        except Errors.InvalidMovementCommandError as err:
            print(err)
            continue
        except Errors.ProgramTerminatedByUser as err:
            print(err)
            break

        # Handler function to control robot in a grid given an input sequence
        controller = Controller(inputSequence, robot, grid)
        try:
            controller.start()
        except Errors.OutOfBoundsError as err:
            print(err)
            continue

if __name__ == "__main__":
    main()