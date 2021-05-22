
"""
    Challenge - Etch A Sketch

    Make a turtle that moves forward, backward, clockwise, counter-clockwise, and
    then clear all the drawing

    W = Forwards
    S = Backwards
    A = Counter-Clockwise
    D = Clockwise
    C = Clear the screen

"""

import turtle


def move_forwards():
    """ Move turtle forward by 10 pixels """
    tim.forward(10)


def move_backwards():
    """ Move turtle backward by 10 pixels """
    tim.back(15)


def move_left():
    """ Turn turtle left by 10 degrees """
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_right():
    """ Turn turtle right by 10 degrees """
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clearDrawings():
    """ Clear the screen and move turtle to the initial position """
    tim.home()
    tim.clear()


tim = turtle.Turtle()
screen = turtle.Screen()

# Make screen to listen to the key events
screen.listen()

# Turtle built-in key press function that takes func and key as inputs
screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# Clear the screen
screen.onkey(clearDrawings, "c")


# Click on screen to exit the game
screen.exitonclick()

