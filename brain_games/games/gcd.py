import random


# -- Description
DESCRIPTION = "Find the greatest common divisor of given numbers."

# -- Parameters
MIN = 1
MAX = 100


def _get_gcd(number_1, number_2):
    # more: https://en.wikipedia.org/wiki/Euclidean_algorithm
    # q_n1 = number_1 // number_2 -- is not necessary
    r_n1 = number_1 % number_2
    if r_n1 == 0:
        return number_2
    return _get_gcd(number_2, r_n1)


# -- Task generator
def generate_task():
    number_1, number_2 = sorted(
        random.sample(range(MIN, MAX + 1), 2),
        reverse=True)
    question = "{} {}".format(number_1, number_2)

    right_answer = _get_gcd(number_1, number_2)

    return question, str(right_answer)
