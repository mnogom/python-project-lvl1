import random

from brain_games import help_functions


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN PROGRESSION ═══{end}\n\n"
               "  - Answer '{green}yes{end}' if given "
               "number is prime. "
               "Otherwise answer '{green}no{end}'.")
DESCRIPTION = help_functions.colorize_string(DESCRIPTION)


# -- Task generator
def task_generator():
    # 'current_number' here is the question
    current_number = random.randint(0, 100)
    simple_numbers = [
        2,  3,  5,  7, 11,
        13, 17, 19, 23, 29,
        31, 37, 41, 43, 47,
        53, 59, 61, 67, 71,
        73, 79, 83, 89, 97]
    right_answer = "yes" if current_number in simple_numbers else "no"

    return current_number, right_answer
