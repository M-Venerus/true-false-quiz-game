#TODO Create QuizBrain class. 3 functions: Ask questions, check if answer was correct, check if at the end of the game.

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.correct_answers = 0
        self.questions_list = q_list

    def next_question(self):
        self.current_question = self.questions_list[self.question_number].text
        self.current_answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number}: {self.current_question} (True/False)?:")
        self.check_answer(self.user_answer, self.current_answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's right!")
            self.correct_answers += 1
        else: 
            print("Sorry, that's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.correct_answers}/{self.question_number}.\n")

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def end_of_game(self):
        print(f"GAME OVER!\nYour final score is {self.correct_answers}/{self.question_number}.")




