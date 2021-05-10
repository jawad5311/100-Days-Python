"""
    Challenge - Turtle Race

"""

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win? Enter Turtle color:")

colors = ["orange", "yellow", "red", "green", "blue", "purple"]

y = -100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    x = -230
    y += 30
    new_turtle.goto(x, y)


#tim = Turtle()

# Click on screen to exit the game
screen.exitonclick()
