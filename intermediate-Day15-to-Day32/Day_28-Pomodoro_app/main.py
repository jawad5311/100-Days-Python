
import math
import tkinter


# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    """ Reset the App when reset button is clicked """
    global reps
    window.after_cancel(timer)  # Tkinter builtin func to stop after() func
    label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 32, "bold"))  # Updates Timer label
    reps = 0
    canvas.itemconfigure(timer_text, text=f"00:00")  # Reset the displaying time
    tick_label.config(text="")  # Reset the tick marks


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    """ Start the timer when start button is clicked """
    global reps
    reps += 1  # Increase the reps everytime timer starts

    # Converts working and break minutes into seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Check for the reps and display work and break text accordingly
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec) 
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    """ Holds all the functionality of counting """
    count_min = math.floor(count / 60)  # Converts the counting sec to min to make them display on the screen like clock
    count_sec = count % 60  # Holds the remaining sec to make them display on the screen0

    # Use to display two digits on screen instead of 1 if the remaining seconds are less then 10
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")  # Display the updated time every 1 sec

    # Decrease the count by 1 after each second
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:  # If the count get to the zero then trigger the start_timer() again
        start_timer()

        # Display the tick mark for each work session completed
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"

        tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


# Create and setup display screen
window = tkinter.Tk()
window.title("PomoDoro App")
window.config(padx=100, pady=50, bg=YELLOW)


"""
    Following are Button and Text properties that are displaying on the screen   
"""

# "Timer" Text
label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
label.grid(column=1, row=0)

# Background image of Tomato
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tomato_img)

# Clock time 00:00
timer_text = canvas.create_text(102, 130, text=f"00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_btn = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(column=0, row=3)

# Reset Button
reset_btn = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_btn.grid(column=2, row=3)

# Tick mark properties
tick_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
tick_label.grid(column=1, row=4)


window.mainloop()  # tkinter built-in func(), Keep the display open until closed
