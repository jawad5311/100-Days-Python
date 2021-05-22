
import tkinter
import quiz_brain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: quiz_brain.QuizBrain):
        self.window = None
        self.quiz = quiz_brain
        self.create_ui_window()
        self.score = 0
        self.score_object()
        self.canvas_object()
        self.get_next_question()
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
        score_label = tkinter.Label(
            text=f"Score: {self.score}",
            bg=THEME_COLOR,
            fg="white"
        )
        score_label.grid(column=1, row=0)

    def canvas_object(self):
        self.canvas = tkinter.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            text="hello",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(
            column=0,
            row=1,
            padx=20,
            pady=30,
            columnspan=2
        )

    def true_btn(self):
        right_btn = tkinter.Button(
            image=self.right_btn_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.right_answer
        )
        right_btn.grid(column=0, row=2, pady=10)

    def wrong_btn(self):
        left_btn = tkinter.Button(
            image=self.left_btn_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.wrong_answer
        )
        left_btn.grid(column=1, row=2, pady=10)

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def right_answer(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def wrong_answer(self):
        self.quiz.check_answer("False")
        self.get_next_question()

