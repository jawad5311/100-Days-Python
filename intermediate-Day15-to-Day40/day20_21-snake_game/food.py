import random
from turtle import Turtle


# Food class inherited from the Turtle class
class Food(Turtle):
    """ Creates food object on the screen """
    def __init__(self):
        super().__init__()  # Inherits all the functionality of Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(.5, .5)  # Decrease the size of the food object by half
        self.color("blue")
        self.speed("fastest")
        # Generate random x and y co-ordinates for the food to place
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)
