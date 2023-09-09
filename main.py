import question_model
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_q = question_model.Question(question["question"], question["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your Final Score is : {quiz.score}/12")