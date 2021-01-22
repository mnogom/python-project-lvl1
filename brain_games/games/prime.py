"""Description of the rules for game 'brain-prime'."""

import random


# -- Description
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

# -- Constants
MIN = 0
MAX = 100


def _is_prime(number: int) -> bool:
    """Check if number is prime.

    It uses Sieve of Eratosthenes conception.
    More: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    :param number: number to check
    :return: True/False
    """

    if number == 0 or number == 1:
        return False

    all_numbers = list(range(2, number + 1))

    while len(all_numbers) != 1:
        simple_number = all_numbers.pop(0)
        all_numbers = [el for el in all_numbers if el % simple_number != 0]

        if number not in all_numbers:
            return False

    return True


# -- Task generator
def generate_round() -> (str, str):
    """Generate question and right answer.

    :return: question and answer
    """

    number = random.randint(MIN, MAX)
    question = str(number)
    right_answer = "yes" if _is_prime(number) else "no"

    return question, right_answer
