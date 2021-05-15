
import turtle


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answer_state = screen.textinput("Guess the State", "What's another state's name?")


screen.exitonclick()
