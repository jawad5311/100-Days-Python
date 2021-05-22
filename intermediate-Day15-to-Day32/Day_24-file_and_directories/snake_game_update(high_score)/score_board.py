
import turtle

# Constants used in ScoreBoard class
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class ScoreBoard(turtle.Turtle):
    """ Creates Score Board and calculates Scores """
    """ Inherited from the Turtle class """
    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide turtle object and only show text
        self.color("white")
        self.penup()
        self.goto(0, 280)  # Make Turtle goto the top
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.update_scoreboard()  # Calls the func

    def read_high_score(self):
        """ Reads the previous high scores from the file """
        with open("data.txt") as file:
            new_high_score = file.read()
            self.high_score = int(new_high_score)

    def update_scoreboard(self):
        """ Updates the Score Board"""
        self.clear()
        text = f"Score: {self.score} High Score: {self.high_score}"
        self.write(text, False, ALIGNMENT, FONT)

    def update_score(self):
        """ Updates the Scores and Score Board """
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        """ Reset Scores and Update high score """
        if self.score > int(self.high_score):
            self.high_score = self.score
            # Writes new high scores to the file data.txt
            with open("data.txt", "w") as file:
                self.high_score = str(self.high_score)
                file.write(self.high_score)

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """ Display Game Over on the screen when snake collide with wall or tail """
    #     self.goto(0, 0)
    #     text = f"Game Over! :("
    #     self.write(text, False, ALIGNMENT, FONT)

