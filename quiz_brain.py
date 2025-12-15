class QuizBrain:
    def __init__(self, question_list):
        self.true_answer = None
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self,):
        question = self.question_list[self.question_number]
        self.question_number += 1
        self.true_answer = question.answer
        user_answer = input(f"Q{self.question_number}: {question.question} ('True' or 'False')").capitalize()

        if self.check_answer(user_answer):
            self.score += 1
            print("You got it right")

        else: print("That's wrong.")


        print(f"The correct answer was: {self.true_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer,):
        return user_answer == self.true_answer


