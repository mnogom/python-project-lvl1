"""
Description of the rules for game 'brain-progression'
"""

import random


# -- Description
DESCRIPTION = "What number is missing in the progression?"

# -- Constants
FIRST_MIN = 0
FIRST_MAX = 100
LENGTH_MIN = 5
LENGTH_MAX = 10
STEP_MIN = 1
STEP_MAX = 100


def _generate_progression(start: int, step: int, length: int) -> list:
    """
    Function returns an arithmetic progression

    :param start: first number of progression
    :param step: step of progression
    :param length: length of progression
    :return: progression
    """

    return [start + i * step for i in range(length)]


# -- Task generator
def generate_task() -> (str, str):
    """
    Generate question and right answer. Uses constants: FIRST_MIN,
    FIRST_MAX, LENGTH_MIN, LENGTH_MAX, STEP_MIN, STEP_MAX

    :return: question and answer
    """

    start = random.randint(FIRST_MIN, FIRST_MAX)
    length = random.randint(LENGTH_MIN, LENGTH_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)

    progression = _generate_progression(start, step, length)

    right_answer = random.choice(progression)
    right_answer_index = progression.index(right_answer)

    progression[right_answer_index] = ".."
    question = " ".join([str(el) for el in progression if el])

    return question, str(right_answer)
