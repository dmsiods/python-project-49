#!usr/bin/env python3
from prompt import string
from random import randint, choice


def get_correct_answer(first_number, second_number, operator):
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


def main():
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print('What is the result of the expression?')

    choices = ['+', '-', '*']

    for _ in range(3):
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        operator = choice(choices)
        print(f'Question: {str(first_number)} {operator} {str(second_number)}')

        user_answer = string('Your answer: ')
        correct_answer = get_correct_answer(first_number, second_number,
                                            operator)

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {user_name}!')
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
