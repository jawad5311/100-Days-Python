
import turtle



def move_up():
    new_y = tim.ycor() + 10
    tim.sety(new_y)


def move_down():
    new_y = tim.ycor() - 10
    tim.sety(new_y)



screen = turtle.Screen()
screen.setup(800, 600)  # Setup screen size Width x Height (800 x 600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)


tim = turtle.Turtle()

tim.shape("square")
tim.color("white")
tim.shapesize(5, 1)
tim.penup()
tim.goto(350, 0)


screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")


game_on = True
while game_on:
    screen.update()

screen.exitonclick()
