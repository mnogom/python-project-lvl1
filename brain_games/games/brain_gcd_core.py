import random

from brain_games import help_functions


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN GCD ═══{end}\n\n"
               "  - Find the greatest common divisor "
               "of given numbers.")
DESCRIPTION = help_functions.colorize_string(DESCRIPTION)

# -- Parameters
MIN = 1
MAX = 100

# more: https://en.wikipedia.org/wiki/Euclidean_algorithm
def _gcd_euclidean(number_1, number_2):
    # q_n1 = number_1 // number_2 -- is not necessary
    r_n1 = number_1 % number_2
    if r_n1 == 0:
        return number_2
    return _gcd_euclidean(number_2, r_n1)


# -- Task generator
def task_generator():
    number_1, number_2 = sorted(
        random.sample(range(MIN, MAX + 1), 2),
        reverse=True)
    question = "{} {}".format(number_1, number_2)

    right_answer = _gcd_euclidean(number_1, number_2)
    right_answer = str(right_answer)

    return question, right_answer
