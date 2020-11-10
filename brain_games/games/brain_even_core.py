import random

from brain_games import help_functions


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN EVEN ═══{end}\n\n"
               "  - Answer '{green}yes{end}' if the number is even,"
               " otherwise answer '{green}no{end}'.")
DESCRIPTION = help_functions.colorize_string(DESCRIPTION)

# -- Parameters
MIN = 0
MAX = 100

# -- Task generator
def task_generator():
    # 'current_number' here is the question
    current_number = random.randint(MIN, MAX + 1)
    right_answer = "no" if current_number % 2 else "yes"

    return current_number, right_answer
