from prompt import string


def welcome_user():
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
