from brain_games.games.abstract_game import AbstractGame
from random import randint


class GcdGame(AbstractGame):
    DEFAULT_TASK_TEXT = 'Find the greatest common divisor of given numbers.'

    def __init__(self, task=None, round_count=None):
        super().__init__(task or self.DEFAULT_TASK_TEXT, round_count)

    def get_question(self):
        first_number = randint(1, 100)
        second_number = randint(1, 100)

        question_text = f'Question: {str(first_number)} {second_number}'
        question_params = (first_number, second_number)

        return question_text, question_params

    def get_correct_answer(self, first_number, second_number):
        if first_number < second_number:
            first_number, second_number = second_number, first_number

        while True:
            if first_number % second_number == 0:
                result = second_number
                break
            else:
                remainder = first_number % second_number
                first_number, second_number = second_number, remainder

        return str(result)
