"""
    Challenge - Turtle Race

    >>> User bet on any turtle from the available turtles of different colors

    >>> Then the turtles Race begins to the finish line

    >>> Print which turtle won and also if the user has won or lost?

"""

from turtle import Turtle, Screen
import random

# variable responsible to stop the race
is_race_on = False

# Creating screen object for turtle
screen = Screen()
screen.setup(width=500, height=400)

# Takes the user input on turtle screen
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win? Enter Turtle color:")

# List of turtle colors
colors = ["orange", "yellow", "red", "green", "blue", "purple"]


y = -100  # Use in for loop for turtle position as y co-ordinate
all_turtles = []  # Turtle list that holds different turtle objects

# for loop to create different turtle objects and append these objects into
# all_turtles list
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    x = -230
    y += 30
    # Make each turtle go to it's own position
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)

# Wait for the user to bet to start the game
if user_bet:
    is_race_on = True


# Keep turtles moving forward until anyone of the turtle wins
while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 220:

            is_race_on = False
            winning_color = turtle.pencolor()

            # Prints the message on screen to show the winning turtle
            if winning_color == user_bet:
                print(f"You Won! \nThe {winning_color} turtle is Winner:)")
            else:
                print(f"You Lost! \nThe {winning_color} turtle is Winner:)")

        # Create random distance for each turtle
        distance = random.randint(0, 10)
        turtle.forward(distance)


# Click on screen to exit the game
screen.exitonclick()
