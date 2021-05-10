
import turtle

# Constants used in ScoreBoard class
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class ScoreBoard(turtle.Turtle):
    """ Creates Score Board and calculates Scores """
    """ Inherited from the Turtle class """
    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide turtle object and only show text
        self.color("white")
        self.penup()
        self.goto(0, 280)  # Make Turtle goto the top
        self.score = 0
        self.update_scoreboard()  # Calls the func

    def update_scoreboard(self):
        """ Updates the Score Board"""
        self.clear()
        text = f"Score: {self.score}"
        self.write(text, False, ALIGNMENT, FONT)

    def update_score(self):
        """ Updates the Scores and Score Board """
        self.score += 1
        self.update_scoreboard()


