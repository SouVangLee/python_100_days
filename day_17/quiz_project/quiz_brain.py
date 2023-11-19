class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        question = current_question.question
        user_answer = input(f"Q.{self.question_number}: {question}. (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if correct_answer.lower() == user_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Thats wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def end_game(self):
        print("You've completed the quiz.")
        print(f"Your final score is: {self.score}/{self.question_number}")