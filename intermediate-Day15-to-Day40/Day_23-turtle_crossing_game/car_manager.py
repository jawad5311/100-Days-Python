
"""
    Holds all the functionality of the car object like

        Creating Cars
        Moving cars on screen
        Increasing car speed

"""

import random
import turtle

# Constant variables
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    """ Holds all the functionality of the cars """
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        """ Create a car and append it to all_cars list """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = turtle.Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))  # Gives a random color to the new car
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)  # Moves new cars to the most right of the screen
            self.all_cars.append(new_car)

    def move_cars(self):
        """ Move cars on the screen """
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        """ Increases cars speed """
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
