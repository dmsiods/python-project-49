from abstract_game import AbstractGame
from random import randint, choice


class CalcGame(AbstractGame):
    DEFAULT_TASK_TEXT = 'What is the result of the expression?'
    DEFAULT_OPERATORS = ['+', '-', '*']

    def __init__(self, task=None, round_count=None, operators=None):
        super().__init__(task or self.DEFAULT_TASK_TEXT, round_count)
        self.operators = operators or self.DEFAULT_OPERATORS

    def get_question(self):
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        operator = choice(self.operators)

        question_text = f'Question: {str(first_number)} {operator}' \
                        f' {str(second_number)}'
        question_params = (first_number, second_number, operator)

        return question_text, question_params

    def get_correct_answer(self, first_number, second_number, operator):
        result = 0

        if operator == '+':
            result = first_number + second_number
        elif operator == '-':
            result = first_number - second_number
        elif operator == '*':
            result = first_number * second_number
        else:
            Exception('Error: unknown operator!!!')

        return str(result)
