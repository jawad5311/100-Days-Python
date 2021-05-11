
import turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.level = 0
        text = f"Level: {self.level}"
        self.write(text, False, "center", FONT)
