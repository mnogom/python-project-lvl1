import random

from brain_games import help_functions


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN PROGRESSION ═══{end}\n\n"
               "  - What number is missing in the "
               "progression?")
DESCRIPTION = help_functions.colorize_string(DESCRIPTION)

# -- Parameters
FIRST_MIN = 0
FIRST_MAX = 100
LENGTH_MIN = 5
LENGTH_MAX = 10
STEP_MIN = 1
STEP_MAX = 100


# -- Task generator
def task_generator():
    prog_start = random.randint(FIRST_MIN, FIRST_MAX)
    prog_length = random.randint(LENGTH_MIN, LENGTH_MAX)
    prog_step = random.randint(STEP_MIN, STEP_MAX)
    prog = [prog_start + i * prog_step for i in range(prog_length)] 

    right_answer = random.choice(prog)
    right_answer_index = prog.index(right_answer)
    right_answer = str(right_answer)

    prog[right_answer_index] = "." * len(right_answer)
    question = " ".join([str(el) for el in prog if el])

    return question, right_answer
