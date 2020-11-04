import random

from brain_games import help_functions


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN CALC ═══{end}\n\n"
               "  - What is the result of the expression?")
DESCRIPTION = help_functions.colorize_string(DESCRIPTION)


# -- Task generator
def task_generator():
    number_1, number_2 = random.sample(range(101), 2)
    operation = random.choice(["+", "-", "*"])
    question = "{n1} {op} {n2}".format(
        n1=number_1,
        n2=number_2,
        op=operation)

    if operation == "+":
        right_answer = number_1 + number_2

    elif operation == "-":
        right_answer = number_1 - number_2

    else:
        right_answer = number_1 * number_2

    right_answer = str(right_answer)

    return question, right_answer
