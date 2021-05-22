
import tkinter
import quiz_brain


# CONSTANTS
THEME_COLOR = "#375362"


class QuizInterface:
    """ Holds all the functionality of User Interface like:
            Creating Interface
            Displaying next question
            Giving feedback on Right or Wrong question
    """
    def __init__(self, quiz_brain: quiz_brain.QuizBrain):
        self.window = None
        self.quiz = quiz_brain
        self.create_ui_window()
        self.canvas = None
        self.score_object()
        self.canvas_object()
        self.get_next_question()
        self.right_btn_img = tkinter.PhotoImage(file="images/true.png")
        self.left_btn_img = tkinter.PhotoImage(file="images/false.png")
        self.true_btn()
        self.wrong_btn()
        self.window.mainloop()

    def create_ui_window(self):
        """ Creates initial window from tkinter """
        self.window = tkinter.Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    def score_object(self):
        """ Creates Score label """
        self.score_label = tkinter.Label(
            text=f"Score: {self.quiz.score}",
            bg=THEME_COLOR,
            fg="white"
        )
        self.score_label.grid(column=1, row=0)

    def canvas_object(self):
        """ Create canvas object containing Question Text """
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
        """ Creates Right Button """
        self.right_btn = tkinter.Button(
            image=self.right_btn_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.right_answer
        )
        self.right_btn.grid(column=0, row=2, pady=10)

    def wrong_btn(self):
        """ Creates Wrong Button """
        self.left_btn = tkinter.Button(
            image=self.left_btn_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.wrong_answer
        )
        self.left_btn.grid(column=1, row=2, pady=10)

    def get_next_question(self):
        """ Display next question on screen """
        self.canvas.config(self.canvas, bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"Quiz Completed! Your Final Score is "
                     f"{self.quiz.score}/{len(self.quiz.question_list)}"
            )

            # Disable Right & Wrong buttons functionality
            self.right_btn.config(
                state="disabled"
            )
            self.left_btn.config(
                state="disabled"
            )

    def right_answer(self):
        """ Checks if user is right & return bool """
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        """ Checks if user is right & return bool """
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """ Provide feedback to the user based on their answer """
        if not is_right:
            self.canvas.config(bg="red")
        if is_right:
            self.canvas.config(bg="green")

        self.score_label.config(
            text=f"Score: {self.quiz.score}"
        )
        self.window.after(1000, self.get_next_question)  # Wait for 1 sec then display next question
