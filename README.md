## Startup:
`python Main.py`

## Testing:
`python Test.py`

## Given that:
- Dimensions of grid are 10 by 10
- Commands are separated by whitespace
- Commands always in capital letter

## Explicit Requirements: 
- Robot does not move outside of warehouse
- User has a way to send commands to robot

## Implicit Requirements / Assumptions:
- To make sure it doesn't move outside the warehouse, we need a starting position for the robot
- We should define some coordinate system for the layout of the warehouse. The starting position should be somewhere inside the warehouse.
- It might also be benefical to the user to also know the sequence of current position of the robot after every step (and also for us to debug)

## Inputs:
- User enters a string of commands, as well as the starting x position and y position of the robot in the grid
- Parsing logic is handled separately in another function. This will handle incorrect user input.

## Features to meet requirements:
- Makes sense for user to know the last known position of the robot
- If one of the commands are invalid, eg. will take robot out of bounds, the robot will perform all the commands up until failure, and ignore all those that come after failure
- We can achieve this by printing the location of the robot to stdout everytime the location is updated, or alternatively, the user can enter a separate command to show the robot's current position
- The program will continue to prompt the user for another string of commands, regardless of success or failure
- Invalid commands or inputs are handled gracefully, and will allow the user to try again
- There is an option for the user to exit the program gracefully
- Outside of the given attributes, program should handle edge cases whenever it asks for user input
- Validation to be performed before movement is performed to ensure that bounds are not exceeded
- Handle this scenario should it occur, by stopping the robot at the last successful command and showing some output to the user indicating the reason for stopping

