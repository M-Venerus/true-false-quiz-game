from question_model import Question 
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_game = QuizBrain(question_bank)

while quiz_game.still_has_questions():
    quiz_game.next_question()

quiz_game.end_of_game()

