
import turtle
import paddle
import ball
import time


screen = turtle.Screen()
r_paddle = paddle.Paddle()
l_paddle = paddle.Paddle()
ball = ball.Ball()


screen.setup(800, 600)  # Setup screen size Width x Height (800 x 600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)


r_paddle.go_to(350, 0)
l_paddle.go_to(-350, 0)

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


game_on = True
while game_on:
    time.sleep(.1)

    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()
