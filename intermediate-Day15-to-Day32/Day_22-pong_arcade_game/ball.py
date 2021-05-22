
import turtle


class Ball(turtle.Turtle):
    """ Create ball object, move, bounce, and reset it's position """
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()  # Make ball not to draw lines on screen
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """ Makes ball move forwards and change it's position """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """ Bounce back the ball if collided with y axis """
        self.y_move *= -1

    def bounce_x(self):
        """ Bounce back the ball if collided with x axis and increase speed """
        self.x_move *= -1
        self.move_speed *= .95

    def ball_reset(self):
        """ Reset the ball position and throw it in the opposite direction """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
