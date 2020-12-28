import random


# -- Description
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

# -- Parameters
MIN = 0
MAX = 100


# -- Task generator
def generate_task():
    question = random.randint(MIN, MAX + 1)
    right_answer = "no" if question % 2 else "yes"

    return question, right_answer
