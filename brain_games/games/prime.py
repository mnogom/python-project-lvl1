import random


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN PROGRESSION ═══{end}\n\n"
               "  - Answer {green}yes{end} if given "
               "number is prime. "
               "Otherwise answer {green}no{end}.\n")

# -- Parameters
MIN = 2
MAX = 100


def _is_prime(number):
    all_numbers = list(range(2, number + 1))

    while len(all_numbers) != 1:
        simple_number = all_numbers.pop(0)
        all_numbers = [el for el in all_numbers if el % simple_number != 0]
        if number not in all_numbers:
            return "no"

    return "yes"


# -- Task generator
def generate_task():
    # 'current_number' here is the question
    question = random.randint(MIN, MAX + 1)
    right_answer = _is_prime(question)

    return question, right_answer
