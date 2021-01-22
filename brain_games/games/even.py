"""Description of the rules for game 'brain-even'."""

import random


# -- Description
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

# -- Constants
MIN = 0
MAX = 100


def _is_even(number: int) -> bool:
    """Check if number is even.

    :param number: number to check
    :return: True/False
    """

    return False if number % 2 else True


# -- Task generator
def generate_round() -> (str, str):
    """Generate question and right answer.

    :return: question and answer
    """

    number = random.randint(MIN, MAX)
    question = str(number)
    right_answer = "yes" if _is_even(number) else "no"

    return question, right_answer
