import random

from brain_games import help_functions


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN PROGRESSION ═══{end}\n\n"
               "  - Answer '{green}yes{end}' if given "
               "number is prime. "
               "Otherwise answer '{green}no{end}'.")
DESCRIPTION = help_functions.colorize_string(DESCRIPTION)

# -- Parameters
MIN = 1
MAX = 100

# -- Task generator
def task_generator():
    # 'current_number' here is the question
    question = random.randint(MIN, MAX + 1)
    SIMPLE_NUMBERS = [
        2,  3,  5,  7, 11,
        13, 17, 19, 23, 29,
        31, 37, 41, 43, 47,
        53, 59, 61, 67, 71,
        73, 79, 83, 89, 97]
    right_answer = "yes" if question in SIMPLE_NUMBERS else "no"

    return question, right_answer
