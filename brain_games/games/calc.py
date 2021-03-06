"""Description of the rules for game 'brain-calc'."""

import random

# -- Description
DESCRIPTION = "What is the result of the expression?"

# -- Constants
MIN = 0
MAX = 100
OPERATIONS = "+-*"


def _calculate_result(number_1: int, number_2: int, operation: str) -> int:
    """Returns result of calculation a mathematical expression.

    :param number_1: number #1
    :param number_2: number #2
    :param operation: mathematical operation
    :return: result of expression
    """

    if operation == "+":
        return number_1 + number_2
    if operation == "-":
        return number_1 - number_2
    if operation == "*":
        return number_1 * number_2

    raise ValueError("Action on '{operation}' is not defined. ".format(
        operation=operation))


# -- Task generator
def generate_round() -> (str, str):
    """Generate question and right answer.

    :return: question and answer
    """

    number_1 = random.randint(MIN, MAX)
    number_2 = random.randint(MIN, MAX)
    operation = random.choice(OPERATIONS)

    question = "{n1} {op} {n2}".format(
        n1=number_1,
        n2=number_2,
        op=operation)

    right_answer = _calculate_result(number_1, number_2, operation)

    return question, str(right_answer)
