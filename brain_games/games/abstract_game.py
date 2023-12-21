from abc import ABC, abstractmethod
from prompt import string


class AbstractGame(ABC):
    DEFAULT_ROUND_COUNT = 3

    def __init__(self, task, round_count):
        self.task = task
        self.round_count = round_count or self.DEFAULT_ROUND_COUNT
        self.user_name = None

    def _greeting(self):
        print('Welcome to the Brain Games!')
        self.user_name = string('May I have your name? ')
        print(f'Hello, {self.user_name}!')

    @abstractmethod
    def get_question(self):
        pass

    @abstractmethod
    def get_correct_answer(self, *args):
        pass

    def process_game(self):
        self._greeting()

        print(self.task)

        for _ in range(self.DEFAULT_ROUND_COUNT):
            question_text, question_params = self.get_question()
            print(question_text)

            user_answer = string('Your answer: ')
            correct_answer = self.get_correct_answer(*question_params)

            if user_answer == correct_answer:
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'.")
                print(f'Let\'s try again, {self.user_name}!')
                break
        else:
            print(f'Congratulations, {self.user_name}!')
