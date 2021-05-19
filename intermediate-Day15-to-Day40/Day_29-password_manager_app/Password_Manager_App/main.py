
import tkinter


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager App")
window.config(padx=20, pady=20)

lock_image = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


"""
    Buttons, Labels, and Entries

"""

label_1 = tkinter.Label(text="Website:")
label_1.grid(column=0, row=1)

label_2 = tkinter.Label(text="Email:")
label_2.grid(column=0, row=2)

label_3 = tkinter.Label(text="Password:")
label_3.grid(column=0, row=3)

web_entry = tkinter.Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)

mail_entry = tkinter.Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2)

pass_entry = tkinter.Entry(width=17)
pass_entry.grid(column=1, row=3)

generate_btn = tkinter.Button(text="Generate Password")
generate_btn.grid(column=2, row=3)

add_btn = tkinter.Button(text="Add", width=35)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
