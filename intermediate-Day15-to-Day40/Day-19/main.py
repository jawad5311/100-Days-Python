
import turtle


tim = turtle.Turtle()
screen = turtle.Screen()


def moveForwards():
    tim.forward(10)


screen.listen()
screen.onkey(moveForwards, "space")
screen.exitonclick()
