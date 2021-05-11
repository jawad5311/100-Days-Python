
import turtle


PADDLE_SPEED = 15


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()

    def go_to(self, x_cor, y_cor):
        self.goto(x_cor, y_cor)

    def move_up(self):
        new_y = self.ycor() + PADDLE_SPEED
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - PADDLE_SPEED
        self.sety(new_y)
