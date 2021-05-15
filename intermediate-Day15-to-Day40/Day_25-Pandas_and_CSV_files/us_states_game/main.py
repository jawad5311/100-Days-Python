
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim = turtle.Turtle()

correct_guesses = []

states_data = pd.read_csv("50_states.csv")

check = len(correct_guesses) < len(states_data.state)
score = 0
total_score = len(states_data.state)

while check:
    text = f"{score}/{total_score} States Correct"
    answer_state = screen.textinput(text, "What's another state's name?").title().strip()
    print(type(answer_state))
    guessed_state = states_data[states_data["state"] == answer_state]
    if check:
        tim.goto(int(guessed_state.x), int(guessed_state.y))
        tim.write(f"{answer_state}")
        correct_guesses.append(answer_state)
        print(correct_guesses)
        score += 1



screen.exitonclick()
