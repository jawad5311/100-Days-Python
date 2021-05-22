
import random
import tkinter
import pandas


# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"


# Global Variables
rand_word = None


"""
    Opening the data file and reading data from it
"""
try:  # Try to open the words_to_learn.csv file
    data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:  # And If the file was not found then open the initial data file
    data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")


"""
    Generating a new random word and updating the existing data
"""
def generate_word():
    """ Generates a random word from the available french words list"""
    global rand_word

    def display_eng_word():
        """ Display the english word of the current french word """
        en_word = rand_word["English"]  # Grabs the English word of the current word
        canvas.itemconfig(card_title, text="English", fill="white")  # Change screen title to English
        canvas.itemconfig(card_word, text=en_word, fill="white")  # Display the english word of the current displaying french word
        canvas.itemconfig(canvas_image, image=back_image)  # Changes the background

    rand_word = random.choice(data)  # Choose a random word from the data

    fr_word = rand_word["French"]  # Grabs the French word of the current word
    canvas.itemconfig(canvas_image, image=front_image)  # Changes the background
    canvas.itemconfig(card_title, text="French", fill="black")  # Change screen title to French
    canvas.itemconfig(card_word, text=fr_word, fill="black")  # Display the french word
    canvas.after(3000, display_eng_word)  # Wait for 3sec and call the function to display english word


def known_word():
    """ Updates the .csv file if the word is known to user and generate a new word """
    global rand_word
    data.remove(rand_word)  # Removes the current random word from the data
    to_learn = pandas.DataFrame(data)  # Creates a data frame of the updated data
    to_learn.to_csv("data/words_to_learn.csv", index=False)  # Creates & Updates the .csv file with updated data
    generate_word()


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
canvas_image = canvas.create_image(400, 263, image=front_image)
#canvas.create_image(400, 263, image=back_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Right and Wrong Buttons
right_btn = tkinter.Button(image=right_image, command=known_word, highlightthickness=0, bg=BACKGROUND_COLOR)
right_btn.grid(column=1, row=1)
wrong_btn = tkinter.Button(image=wrong_image, command=generate_word, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_btn.grid(column=0, row=1)

generate_word()  # Generates the initial word on the screen

window.mainloop()  # Keep window running
