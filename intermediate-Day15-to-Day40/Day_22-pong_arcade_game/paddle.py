
import turtle

# Constants variables
PADDLE_SPEED = 15


class Paddle(turtle.Turtle):
    """ Creates and Move paddles on the screen """
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)  # Resize the object into paddle shape (width x length)
        self.penup()

    def go_to(self, x_cor, y_cor):
        """ Requires integers value for x and y co-ordinates """
        self.goto(x_cor, y_cor)

    def move_up(self):
        """ Make paddle move upwards """
        new_y = self.ycor() + PADDLE_SPEED
        self.sety(new_y)

    def move_down(self):
        """ Make paddle move downwards """
        new_y = self.ycor() - PADDLE_SPEED
        self.sety(new_y)
