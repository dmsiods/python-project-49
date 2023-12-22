from brain_games.games.abstract_game import AbstractGame
from random import randint


class ProgressionGame(AbstractGame):
    DEFAULT_TASK_TEXT = 'What number is missing in the progression?'
    DEFAULT_NUM_COUNT = 10

    def __init__(self, task=None, round_count=None, num_count=None):
        super().__init__(task or self.DEFAULT_TASK_TEXT, round_count)
        self.num_count = num_count or self.DEFAULT_NUM_COUNT

    def get_question(self):
        first_number = randint(1, 100)
        step = randint(1, 20)
        missing_idx = randint(0, self.num_count - 1)
        numbers = []

        for i in range(self.num_count):
            numbers.append(str(first_number + i * step))

        missing_num = numbers[missing_idx]
        numbers[missing_idx] = '..'

        question_text = 'Question: ' + ' '.join(numbers)
        question_params = (numbers, missing_num)

        return question_text, question_params

    def get_correct_answer(self, numbers, missing_num):
        return missing_num
