import random


# -- Description
DESCRIPTION = ("{blue}═══ BRAIN EVEN ═══{end}\n\n"
               "  - Answer {green}yes{end} if the number is even,"
               " otherwise answer {green}no{end}.\n")

# -- Parameters
MIN = 0
MAX = 100


# -- Task generator
def generate_task():
    question = random.randint(MIN, MAX + 1)
    right_answer = "no" if question % 2 else "yes"

    return question, right_answer
