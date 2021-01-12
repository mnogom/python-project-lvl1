"""
Description of the rules for game 'brain-calc'
"""

import random
import operator


# -- Description
DESCRIPTION = "What is the result of the expression?"

# -- Constants
MIN = 0
MAX = 100
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}


def _calculate_result(number_1: int, number_2: int, operation: str) -> int:
    """
    Returns result of calculation a mathematical expression

    :param number_1: number #1
    :param number_2: number #2
    :param operation: mathematical operation
    :return: result of expression
    """

    return OPERATIONS[operation](number_1, number_2)


# -- Task generator
def generate_task() -> (str, str):
    """
    Generate question and right answer. Uses constants: MIN, MAX, OPERATIONS

    :return: question and answer
    """

    number_1, number_2 = random.sample(range(MIN, MAX + 1), 2)
    operation = random.choice(list(OPERATIONS.keys()))

    question = "{n1} {op} {n2}".format(
        n1=number_1,
        n2=number_2,
        op=operation)

    right_answer = _calculate_result(number_1, number_2, operation)

    return question, str(right_answer)
