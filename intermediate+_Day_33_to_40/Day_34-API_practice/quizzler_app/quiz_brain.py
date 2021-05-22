
import html  # To format or unescape the fetched data


class QuizBrain:
    """ Receive question list and hold this list properties like:
            No. of questions,
            Show next question,
            Checks the answer
    """
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """ Returns True if the question no. is less then length of question list"""
        return self.question_number < len(self.question_list)  # Returns bool (True / False)

    def next_question(self) -> str:
        """ Shows the next question from the list """
        self.current_question = self.question_list[self.question_number]  # Hold the question from list using question_number as index
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)  # Format the question in human readable form
        return f"Q.{self.question_number}: {q_text} (True/False): "  # Returns question text
        # self.check_answer(user_answer)

    def check_answer(self, user_answer) -> bool:
        """ Takes user answer and matches it with correct answer and return True if correct """
        correct_answer = self.current_question.answer  # Holds the correct answer from the current_question object
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
