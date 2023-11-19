from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []

for data in question_data:
    question = data["text"]
    answer = data["answer"]
    question_object = Question(question, answer)
    questions.append(question_object)

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()
quiz.end_game()