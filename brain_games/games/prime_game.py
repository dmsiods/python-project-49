from brain_games.games.abstract_game import AbstractGame
from math import sqrt, ceil
from random import randint


class PrimeGame(AbstractGame):
    DEFAULT_TASK_TEXT = 'Answer "yes" if given number is prime.' \
                        ' Otherwise answer "no".'

    def __init__(self, task=None, round_count=None):
        super().__init__(task or self.DEFAULT_TASK_TEXT, round_count)

    def get_question(self):
        question_number = randint(1, 100)
        question_text = f'Question: {str(question_number)}'

        return question_text, (question_number,)

    def get_correct_answer(self, question_number):
        if question_number == 1:
            return 'no'

        if question_number == 2:
            return 'yes'

        for i in range(2, ceil(sqrt(question_number))):
            if question_number % i == 0:
                return 'no'

        return 'yes'
