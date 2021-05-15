
import turtle
import pandas as pd

# Create screen object and set states_img as background
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # Add user img to the turtle shape list
turtle.shape(image)

# Create turtle object
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

states_data = pd.read_csv("50_states.csv")

# Stores all the correct guessed states
correct_guesses = []
states_list = states_data.state.to_list()

# Checks if user have guessed all the states
check = len(correct_guesses) < len(states_data.state)
total_score = len(states_data.state)

# Keeps loop running while the user have not guessed all the states
while check:
    # Takes user input and display scores on screen
    text = f"{len(correct_guesses)}/{total_score} States Correct"
    answer_state = screen.textinput(text, "What's another state's name?").title().strip()
    guessed_state = states_data[states_data["state"] == answer_state]

    # Ends while loop if user enter exit and create the csv of missing states
    if answer_state == "Exit":
        missing_states = pd.DataFrame(states_list)
        missing_states.to_csv("states_to_learn.csv")
        break

    # Check if guessed state is in states list
    if answer_state in states_data.state.to_list():
        # Make turtle go to the x and y co-ordinates of guessed states
        tim.goto(int(guessed_state.x), int(guessed_state.y))
        tim.write(f"{answer_state}")  # Write the guessed state name
        correct_guesses.append(answer_state)  # append the correct guess in list
        states_list.remove(answer_state)
