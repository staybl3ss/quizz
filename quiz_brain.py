class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_q_txt = current_question.text
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number} {current_q_txt} True or False?: ").lower()
        self.check_answer(user_ans, current_question.ans)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect answer, sorry.")
        print(f"The right answer is: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
