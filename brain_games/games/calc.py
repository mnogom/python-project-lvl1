import random
import operator


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN CALC ═══{end}\n\n"
               "  - What is the result of the expression?\n")

# -- Parameters
MIN = 0
MAX = 100
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}


# -- Task generator
def generate_task():
    number_1, number_2 = random.sample(range(MIN, MAX + 1), 2)
    operation = random.choice(list(OPERATIONS.keys()))
    question = "{n1} {op} {n2}".format(
        n1=number_1,
        n2=number_2,
        op=operation)

    right_answer = OPERATIONS[operation](number_1, number_2)

    return question, str(right_answer)
