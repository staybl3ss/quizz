from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    qst = question["question"]
    ans = question["correct_answer"]
    new_question = Question(qst, ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}!")

    