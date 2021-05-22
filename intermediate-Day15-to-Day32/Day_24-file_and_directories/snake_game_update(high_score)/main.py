
import turtle
import snake
import time
import food
import score_board


screen = turtle.Screen()  # Screen object from turtle module
screen.setup(600, 600)  # Screen Width x Height (600 x 600)
screen.bgcolor("black")  # Set screen background color
screen.title("Snake Game")  # Gives the screen a Title
screen.tracer(0)  # Increase the speed of snake animation

snake = snake.Snake()  # Snake Object from Snake class
food = food.Food()  # Food object from Food class
score = score_board.ScoreBoard()  # Score object from ScoreBoard class

# Make screen listen for the key events and calls the corresponding func()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True  # Keep game running until game over

# Game functionality
while game_on:
    """ This while loop keeps game running and calls all the functionality of game """
    screen.update()  # Screen updates upon calling this func. Turtle internal func
    time.sleep(0.2)
    snake.move()  # Moves snake forward.

    # Check if snake has eaten the food
    if snake.head.distance(food) < 15:
        food.refresh()  # Refresh food on the screen
        snake.extend()  # Increase snake length
        score.update_score()  # Update scores on the screen

    # Check for Wall Collisions
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()  # Reset scores and update high scores
        snake.reset_snake()  # Reset snake body

    # Check for Tail Collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()  # Exit the game screen when clicked
