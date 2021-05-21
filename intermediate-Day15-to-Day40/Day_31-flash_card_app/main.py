
import tkinter



BACKGROUND_COLOR = "#B1DDC6"


















"""
    User Interface
"""

window = tkinter.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50)

right_image = tkinter.PhotoImage(file="images/right.png")
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
front_image = tkinter.PhotoImage(file="images/card_front.png")
back_image = tkinter.PhotoImage(file="images/card_back.png")


canvas = tkinter.Canvas(width=800, height=526)
canvas.create_image(400, 263, image=front_image)
canvas.create_image(400, 263, image=back_image)

canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="label", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


word = tkinter.Label(text="Word")
word.grid()

right_btn = tkinter.Button(image=right_image, highlightthickness=0)
right_btn.grid(column=0, row=1)

wrong_btn = tkinter.Button(image=wrong_image)
wrong_btn.grid(column=1, row=1)

window.mainloop()
