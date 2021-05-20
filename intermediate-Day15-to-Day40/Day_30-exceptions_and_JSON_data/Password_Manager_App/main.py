
"""
    Password Manager App

    Stores Website, email, and password to the file locally.
    Also create a random password and copy it to clipboard.

"""

import tkinter
from tkinter import messagebox
import random
import string
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


alphabets = string.ascii_lowercase + string.ascii_uppercase  # Alphabets uppercase + lowercase
characters = [_ for _ in alphabets]  # list of alphabets upper + lower case
digits = [_ for _ in string.digits]  # Digits 0-9
symbols = ['!', '#', '$', '%', '(', ')', '*', '+']


def generate_password():
    """ Generate a random password of 12 to 15 characters"""
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_char = [random.choice(characters) for char in range(nr_letters)]  # Holds random alphabets from characters list
    random_symb = [random.choice(symbols) for sym in range(nr_symbols)]  # Holds random symbols from symbols list
    random_numb = [random.choice(digits) for num in range(nr_numbers)]  # Holds random numbers 0-9 from numbers list

    password_list = random_char + random_numb + random_symb  # Creates a new list containing random characters, sysmbols, and numbers
    random.shuffle(password_list)  # Shuffle the list objects

    password = "".join(password_list)  # Join the list objects and return string

    return password


def add_password():
    """ Add password to the Password Entry & also copy it to clipboard """
    pass_entry.delete(0, tkinter.END)  # Clear the existing password or data in password entry
    random_password = generate_password()  # Calls the function to generate a password
    pass_entry.insert(0, random_password)  # Insert the password in password entry
    pyperclip.copy(random_password)  # Copy the password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """ Saves the entered data into a .txt file """

    # Holds website, email, and password entries data
    website_data = web_entry.get()
    email_data = mail_entry.get()
    pass_data = pass_entry.get()

    new_data = {
        website_data: {
            "email": email_data,
            "password": pass_data
        }
    }

    if len(website_data) == 0 or len(pass_data) == 0:
        messagebox.showinfo(title="Ooops", message="Please fill all the fields")

    # # Pop up the dialog box for the confirmation
    # is_ok = messagebox.askokcancel(title=website_data, message=f"Details Entered:\n\ nEmail: {email_data}\nPassword: {pass_data}\n\n"
    #                                                    f"Check and Press OK to Save!")

    # If confirmed then save the data to file and clear website and password entries
    else:
        with open("data.json", "r") as file:
            data = json.load(file)
            data.update(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
            web_entry.delete(0, tkinter.END)  # Clear website entry
            pass_entry.delete(0, tkinter.END)  # Clear password entry


# ---------------------------- UI SETUP ------------------------------- #


""" Creates UI window and Set up its properties """
window = tkinter.Tk()  # Creates window
window.title("Password Manager App")  # Window title
window.config(padx=50, pady=50)  # Padding from x and y

lock_image = tkinter.PhotoImage(file="logo.png")  # Creates an image file from the location provided to be used as background
canvas = tkinter.Canvas(width=200, height=200)  # Creates a canvas object
canvas.create_image(100, 100, image=lock_image)  # Creates image in canvas object using above created image file
canvas.grid(column=1, row=0)


"""
    Buttons, Labels, and Entries
    
    In the following code:
        First line creates an object (label, button, entry)
        Second line display object on screen (displaying in grid)

"""

label_1 = tkinter.Label(text="Website:")
label_1.grid(column=0, row=1)

label_2 = tkinter.Label(text="Email:")
label_2.grid(column=0, row=2)

label_3 = tkinter.Label(text="Password:")
label_3.grid(column=0, row=3)

web_entry = tkinter.Entry(width=40)
web_entry.grid(column=1, row=1, columnspan=2, sticky="w")
web_entry.focus()  # Move the cursor to the entry box

mail_entry = tkinter.Entry(width=40)
mail_entry.grid(column=1, row=2, columnspan=2, sticky="w")
mail_entry.insert(0, "myName@email.com")  # Insert initial text / data

pass_entry = tkinter.Entry(width=40)
pass_entry.grid(column=1, row=3, columnspan=2, sticky="w")

generate_btn = tkinter.Button(text="Generate Password", command=add_password, width=34)
generate_btn.grid(column=1, row=4)

add_btn = tkinter.Button(text="Add", command=save, width=34)
add_btn.grid(column=1, row=5, columnspan=2, sticky="w")


window.mainloop()  # Keep window running
