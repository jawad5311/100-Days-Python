
"""
    Holds all the functionality of the Score Board like,
        Create score board
        Update score board
        Game over
"""

import turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    """ Holds all the functionality of the Score Board """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)  # Make score board go to the top left corner.
        self.level = 1
        self.show_score()

    def show_score(self):
        """ Show scores on the screen """
        text = f"Level: {self.level}"
        self.write(text, False, "center", FONT)

    def update_score(self):
        """ Update scores """
        self.level += 1
        self.clear()
        self.show_score()

    def game_over(self):
        """ Display Game Over on the screen """
        # self.clear()
        # self.level = 0
        # self.show_score()
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)