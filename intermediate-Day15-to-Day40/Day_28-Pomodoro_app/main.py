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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_sec = 3
    short_break_sec = 2
    long_break_sec = 4

    if reps % 2 == 0:
        count_down(work_sec)
        label.config(text="Working Time", fg=GREEN)
        reps += 1

    elif reps % 2 != 0:

        if reps % 7 == 0:
            count_down(long_break_sec)
            label.config(text="Long Breeeaaakk", fg=RED)
            reps = 0
        else:
            count_down(short_break_sec)
            label.config(text="Break Time", fg=PINK)
            reps += 1

    #
    # else:
    #     count_down(work_sec)
    #     reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("PomoDoro App")
window.config(padx=100, pady=50, bg=YELLOW)


label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
label.grid(column=1, row=0)

tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tomato_img)

timer_text = canvas.create_text(102, 130, text=f"00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_btn = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(column=0, row=3)

reset_btn = tkinter.Button(text="Reset", highlightthickness=0)
reset_btn.grid(column=2, row=3)

new_label = tkinter.Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
new_label.grid(column=1, row=4)



window.mainloop()
