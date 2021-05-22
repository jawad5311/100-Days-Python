
import turtle
import paddle
import ball
import time
import score_board


# Creates screen object for the game
screen = turtle.Screen()

screen.setup(800, 600)  # Setup screen size Width x Height (800 x 600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)  # Removes animations on the screen


# Creating Objects from the created Classes
r_paddle = paddle.Paddle()
l_paddle = paddle.Paddle()
ball = ball.Ball()
score = score_board.ScoreBoard()

# Assign paddles initial position on the board
r_paddle.go_to(350, 0)
l_paddle.go_to(-350, 0)

# Enable screen to listen for the key events
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_on = True

# Keep game running until exit
while game_on:
    # Contains all the functionality of the game
    time.sleep(ball.move_speed)  # Controls ball speed

    screen.update()  # Needs to update screen as the tracer() func is called above
    ball.move()  # Make ball move on the screen

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # If right player misses, reset the ball, increase left player score
    if ball.xcor() > 350:
        ball.ball_reset()
        score.l_point()

    # If left player misses, reset the ball, increase right player score
    if ball.xcor() < -350:
        ball.ball_reset()
        score.r_point()


screen.exitonclick()  # Keep screen on until clicked
