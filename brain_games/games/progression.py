import random


# -- Description
DESCRIPTION = "What number is missing in the progression?"

# -- Parameters
FIRST_MIN = 0
FIRST_MAX = 100
LENGTH_MIN = 5
LENGTH_MAX = 10
STEP_MIN = 1
STEP_MAX = 100


# -- Task generator
def generate_task():
    progression_start = random.randint(FIRST_MIN, FIRST_MAX)
    progression_length = random.randint(LENGTH_MIN, LENGTH_MAX)
    progression_step = random.randint(STEP_MIN, STEP_MAX)
    progression = [progression_start + i * progression_step for i in range(progression_length)]  # noqa: E501

    right_answer = random.choice(progression)
    right_answer_index = progression.index(right_answer)
    right_answer = str(right_answer)

    progression[right_answer_index] = ".."
    question = " ".join([str(el) for el in progression if el])

    return question, right_answer
