"""Description of the rules for game 'brain-gcd'."""

import random


# -- Description
DESCRIPTION = "Find the greatest common divisor of given numbers."

# -- Constants
MIN = 1
MAX = 100


def _get_gcd(number_1: int, number_2: int) -> int:
    """Function return greatest common divisor of two numbers.
    It uses Euclidean algorithm.
    More: https://en.wikipedia.org/wiki/Euclidean_algorithm

    :param number_1: number #1
    :param number_2: number #2
    :return: greatest common divisor
    """

    remainder = number_1 % number_2
    if remainder == 0:
        return number_2
    return _get_gcd(number_2, remainder)


# -- Task generator
def generate_question() -> (str, str):
    """Generate question and right answer. Uses constants: MIN, MAX

    :return: question and answer
    """

    number_1 = random.randint(MIN, MAX)
    number_2 = random.randint(MIN, MAX)
    question = "{} {}".format(number_1, number_2)

    right_answer = _get_gcd(number_1, number_2)

    return question, str(right_answer)
