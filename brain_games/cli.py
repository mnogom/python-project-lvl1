"""Module implements command line interface."""

import prompt


def welcome_user() -> str:
    """Function welcome User and ask him for the name

    :return: User name
    """

    print("Welcome to the Brain Games!")
    username = prompt.string("May I have your name? ")
    print("Hello, {}!".format(username))

    return username
