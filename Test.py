import unittest
from Robot import Robot
from Grid import Grid
from Controller import Controller
import Helper
import Errors


class Test(unittest.TestCase):

    def test_move_success(self):
        # Initialise Robot starting at SouthWest corner
        robot = Robot(0, 0)

        # Initialise Grid object to store attributes of building
        grid = Grid(0, 9)

        # Handler function to control robot in a grid given an input sequence
        controller = Controller(['N', 'E', 'E'], robot, grid)
        controller.start()

        self.assertEqual(robot.getY(), 1, "Final Y coordinate should be 1")
        self.assertEqual(robot.getX(), 2, "Final X coordinate should be 1")

    def test_move_failure(self):
        # Initialise Robot starting at SouthWest corner
        robot = Robot(0, 0)

        # Initialise Grid object to store attributes of building
        grid = Grid(0, 9)

        # Handler function to control robot in a grid given an input sequence
        controller = Controller(['N', 'W'], robot, grid)

        with self.assertRaises(Errors.OutOfBoundsError):
            controller.start()

    def test_invalid_command(self):
        command = "N S E W A B C"

        with self.assertRaises(Errors.InvalidMovementCommandError):
            Helper.parseCommand(command)
        
    def test_no_command(self):
        command = ""

        with self.assertRaises(Errors.NoMovementCommandError):
            Helper.parseCommand(command)


if __name__ == '__main__':
    unittest.main()