
"""
    Turtle Crossing Game - Day 23

    User control the turtle to move forward and avoid collision with cars.
    If the turtle reaches the finish line, Levels up and car speed increases.
    If the turtle collides with any of the car. Game over!
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creates screen object and do initial screen setup
screen = Screen()
screen.setup(600, 600)  # Width x Height (600 x 600)
screen.bgcolor("gray")  # Background color
screen.tracer(0)  # Stops animations. Requires to update screen frequently

# Creating different objects from classes
player = Player()
car_manager = CarManager()
score = Scoreboard()

# Make screen listen to the key events
screen.listen()
screen.onkeypress(player.move_forward, "Up")

""" 
    This while loop holds all the functionality of the game like,
    Player control,
    Create and move cars,
    Update scores and Level up,
    Detect collisions and Game over.
"""
game_on = True
while game_on:
    # Wait for 0.1 sec then update the screen
    time.sleep(0.1)
    screen.update()

    # Create and move cars on the screen
    car_manager.create_car()
    car_manager.move_cars()

    # Check if player has reached the finish line
    if player.ycor() > 280:
        player.reset_turtle()  # Reset turtle position
        score.update_score()  # Update Scores
        car_manager.increase_speed()  # Increase Cars speed

    # Detect turtle collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.game_over()  # Game over


screen.exitonclick()  # Wait for the user response to close the screen
