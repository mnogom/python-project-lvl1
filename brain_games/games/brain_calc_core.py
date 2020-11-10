import random
import operator

from brain_games import help_functions


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN CALC ═══{end}\n\n"
               "  - What is the result of the expression?")
DESCRIPTION = help_functions.colorize_string(DESCRIPTION)

# -- Parameters
MIN = 0
MAX = 100
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}

# -- Task generator
def task_generator():
    number_1, number_2 = random.sample(range(MIN, MAX + 1), 2)
    operation = random.choice(list(OPERATIONS.keys()))
    question = "{n1} {op} {n2}".format(
        n1=number_1,
        n2=number_2,
        op=operation)

    right_answer = OPERATIONS[operation](number_1, number_2)
    right_answer = str(right_answer)

    return question, right_answer
