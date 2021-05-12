
"""
    Hold all the functionality of the player object like,

        Creating turtle,
        move turtle forward,
        reset turtle position

"""

import turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    """ Hold all the functionality of the player object """
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_forward(self):
        """ Move cars forward on the screen """
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        """ RESET turtle position on the screen """
        self.goto(STARTING_POSITION)
