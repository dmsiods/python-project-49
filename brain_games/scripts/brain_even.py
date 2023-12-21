#!usr/bin/env python3
from prompt import string
from random import randint


def main():
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')

    # even number - четное число
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        question_number = randint(1, 100)
        print(f'Question: {str(question_number)}')

        user_answer = string('Your answer: ')
        correct_answer = 'yes' if question_number % 2 == 0 else 'no'

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {user_name}!')
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
