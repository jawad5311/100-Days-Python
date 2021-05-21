import random
import tkinter
import pandas


# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"


"""
    Displaying random word on screen

"""

data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
# print(data)
# print(rand_word)
# print(type(rand_word))
# print(rand_word["French"])
# print(rand_word["English"])

# data.remove(rand_word)


def generate_word():
    rand_word = random.choice(data)
    fr_word = rand_word["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=fr_word)


"""
    User Interface
"""

# Creating window that holds canvas object and buttons
window = tkinter.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images Objects
right_image = tkinter.PhotoImage(file="images/right.png")
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
front_image = tkinter.PhotoImage(file="images/card_front.png")
back_image = tkinter.PhotoImage(file="images/card_back.png")

# Canvas Object that holds background image and Title & Label
canvas = tkinter.Canvas(width=800, height=526)
canvas.create_image(400, 263, image=front_image)
canvas.create_image(400, 263, image=back_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Right and Wrong Buttons
right_btn = tkinter.Button(image=right_image, command=generate_word, highlightthickness=0, bg=BACKGROUND_COLOR)
right_btn.grid(column=0, row=1)
wrong_btn = tkinter.Button(image=wrong_image, command=generate_word, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_btn.grid(column=1, row=1)

generate_word()

window.mainloop()  # Keep window running
