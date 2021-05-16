
import tkinter

# Constant variable
FIX_PAD_X_Y = 10  # Padding for each component on screen

# Creates and set up screen
window = tkinter.Tk()
window.minsize(300, 100)
window.title("Miles to KM Converter")
window.config(padx=40, pady=30)


def calculate_km():
    """ Converts km to miles"""
    miles = round(float(miles_input.get()) * 1.609, 2)
    km_output.config(text=miles)


# Miles input entry on screen
miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0, padx=FIX_PAD_X_Y, pady=FIX_PAD_X_Y)

# Display "Miles" on screen
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0, padx=FIX_PAD_X_Y, pady=FIX_PAD_X_Y)

# Display "is equal to" on screen
equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1, padx=FIX_PAD_X_Y, pady=FIX_PAD_X_Y)

# Display converted output
km_output = tkinter.Label(text="0")
km_output.grid(column=1, row=1, padx=FIX_PAD_X_Y, pady=FIX_PAD_X_Y)

# Display kilometer unit "Km"
km_label= tkinter.Label(text="KM")
km_label.grid(column=2, row=1, padx=FIX_PAD_X_Y, pady=FIX_PAD_X_Y)

# Display Calculate (button)
calc_btn = tkinter.Button(text="Calculate", command=calculate_km)
calc_btn.grid(column=1, row=2, padx=FIX_PAD_X_Y, pady=FIX_PAD_X_Y)


window.mainloop()  # Keep screen open until clicked to close
