
import turtle


class ScoreBoard(turtle.Turtle):
    """ Creates scores and update Score Board """
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()  # Make turtle (score object) not to draw lines on screen
        self.hideturtle()  # Hide turtle so only scores are displayed
        self.score_l = 0
        self.score_r = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        # Updates the Score Board
        self.clear()
        self.goto(-100, 200)
        # Display left player score
        self.write(self.score_l, False, "center", ("Courier", 80, "normal"))
        self.goto(100, 200)
        # Display Right player score
        self.write(self.score_r, False, "center", ("Courier", 80, "normal"))

    def l_point(self):
        """ Increase Left player score """
        self.score_l += 1
        self.update_scoreboard()

    def r_point(self):
        """ Increase Right player score """
        self.score_r += 1
        self.update_scoreboard()
