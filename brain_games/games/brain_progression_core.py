import random

from brain_games import help_functions


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN PROGRESSION ═══{end}\n\n"
               "  - What number is missing in the "
               "progression?")
DESCRIPTION = help_functions.colorize_string(DESCRIPTION)


# -- Task generator
def task_generator():
    prog_start = random.randint(0, 100)
    prog_length = random.randint(5, 10)
    prog_step = random.randint(1, 100)
    prog = [prog_start + i * prog_step for i in range(prog_length)]

    right_answer = random.choice(prog)
    right_answer = str(right_answer)

    question = " ".join([str(el) for el in prog])
    question = question.replace(
        right_answer,
        "." * len(right_answer))

    return question, right_answer
