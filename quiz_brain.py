class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        answer = input(f"Q.{self.question_num} : {current_question.text} (True/False) ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_ans):
        if answer.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"Current score = {self.score}/{self.question_num}")
        print("\n")

