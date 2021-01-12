"""
Description of the rules for game 'brain-prime'
"""

import random


# -- Description
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

# -- Constants
MIN = 2
MAX = 100


def _is_prime(number: int) -> str:
    """
    Function check if number is prime.
    It uses Sieve of Eratosthenes conception.
    More: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    Returns 'yes' if even, 'no' if not

    :param number: number to check
    :return: 'yes'/'no'
    """

    all_numbers = list(range(2, number + 1))

    while len(all_numbers) != 1:
        simple_number = all_numbers.pop(0)
        all_numbers = [el for el in all_numbers if el % simple_number != 0]

        if number not in all_numbers:
            return "no"

    return "yes"


# -- Task generator
def generate_task() -> (str, str):
    """
    Generate question and right answer. Uses constants: MIN, MAX

    :return: question and answer
    """

    # here 'the number' is 'the question'
    number = random.randint(MIN, MAX + 1)
    right_answer = _is_prime(number)

    return str(number), right_answer
