"""
Description of the rules for game 'brain-even'
"""

import random


# -- Description
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

# -- Constants
MIN = 0
MAX = 100


def _is_even(number: int) -> str:
    """
    Check if number is even. Returns 'yes' if even, 'no' if not

    :param number: number to check
    :return: 'yes'/'no'
    """

    return "no" if number % 2 else "yes"


# -- Task generator
def generate_task() -> (str, str):
    """
    Generate question and right answer. Uses constants: MIN, MAX

    :return: question and answer
    """

    number = random.randint(MIN, MAX + 1)
    question = str(number)
    right_answer = _is_even(number)

    return question, right_answer
