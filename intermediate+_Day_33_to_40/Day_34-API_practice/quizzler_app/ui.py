
import tkinter

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = None
        self.create_ui_window()
        self.score = 0
        self.score_object()
        self.canvas_object()
        self.right_btn_img = tkinter.PhotoImage(file="images/true.png")
        self.left_btn_img = tkinter.PhotoImage(file="images/false.png")
        self.true_btn()
        self.wrong_btn()
        self.window.mainloop()

    def create_ui_window(self):
        self.window = tkinter.Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    def score_object(self):
        score_label = tkinter.Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        score_label.grid(column=1, row=0, padx=20, pady=20)

    def canvas_object(self):
        canvas = tkinter.Canvas(width=300, height=250)
        q_text = canvas.create_text(150, 125, text="hello", font=("Arial", 20, "italic"))
        canvas.grid(column=0, row=1, padx=20, pady=20, columnspan=2)

    def true_btn(self):
        right_btn = tkinter.Button(image=self.right_btn_img, highlightthickness=0, bg=THEME_COLOR)
        right_btn.grid(column=0, row=2)

    def wrong_btn(self):
        left_btn = tkinter.Button(image=self.left_btn_img, highlightthickness=0, bg=THEME_COLOR)
        left_btn.grid(column=1, row=2)
