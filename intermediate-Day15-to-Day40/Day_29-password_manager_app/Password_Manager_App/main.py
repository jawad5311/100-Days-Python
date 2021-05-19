
import tkinter


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_data = web_entry.get()
    email_data = mail_entry.get()
    pass_data = pass_entry.get()

    with open("data.txt", "a") as file:
        file.write(f"{website_data} | {email_data} | {pass_data}\n")

    web_entry.delete(0, tkinter.END)
    pass_entry.delete(0, tkinter.END)




# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager App")
window.config(padx=50, pady=50)

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

web_entry = tkinter.Entry(width=40)
web_entry.grid(column=1, row=1, columnspan=2, sticky="w")
web_entry.focus()

mail_entry = tkinter.Entry(width=40)
mail_entry.grid(column=1, row=2, columnspan=2, sticky="w")
mail_entry.insert(0, "myName@email.com")

pass_entry = tkinter.Entry(width=40)
pass_entry.grid(column=1, row=3, columnspan=2, sticky="w")

generate_btn = tkinter.Button(text="Generate Password", width=34)
generate_btn.grid(column=1, row=4)

add_btn = tkinter.Button(text="Add", command=save, width=34)
add_btn.grid(column=1, row=5, columnspan=2, sticky="w")


window.mainloop()
