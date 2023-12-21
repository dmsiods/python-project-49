from brain_games.games.abstract_game import AbstractGame
from random import randint


class EvenGame(AbstractGame):
    DEFAULT_TASK_TEXT = 'Answer "yes" if the number is even,' \
                        ' otherwise answer "no".'

    def __init__(self, task=None, round_count=None):
        super().__init__(task or self.DEFAULT_TASK_TEXT, round_count)

    def get_question(self):
        question_number = randint(1, 100)
        question_text = f'Question: {str(question_number)}'

        return question_text, (question_number,)

    def get_correct_answer(self, question_number):
        return 'yes' if question_number % 2 == 0 else 'no'
