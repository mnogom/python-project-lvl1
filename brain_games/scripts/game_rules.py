import random
import brain_games.scripts.help_functions as hf


def generator_brain_even():
    # -- Description
    DESCRIPTION = ("{blue}═══ BRAIN EVEN ═══{end}\n\n"
                   "  - Answer '{green}yes{end}' if the number is even,"
                   " otherwise answer '{green}no{end}'.")
    DESCRIPTION = hf.colorize_string(DESCRIPTION)

    # -- Task generator
    def task_generator():
        # 'current_number' here is the question
        current_number = random.randint(0, 100)
        right_answer = "no" if current_number % 2 else "yes"

        return current_number, right_answer

    return DESCRIPTION, task_generator


def generator_brain_calc():
    # -- Description
    DESCRIPTION = ("{blue}═══ BRAIN CALC ═══{end}\n\n"
                   "  - What is the result of the expression?")
    DESCRIPTION = hf.colorize_string(DESCRIPTION)

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

    return DESCRIPTION, task_generator


def generator_brain_gcd():
    # -- Description
    DESCRIPTION = ("{blue}═══ BRAIN GCD ═══{end}\n\n"
                   "  - Find the greatest common divisor "
                   "of given numbers.")
    DESCRIPTION = hf.colorize_string(DESCRIPTION)

    # -- Task generator
    def task_generator():
        number_1, number_2 = sorted(
            random.sample(range(1, 101), 2),
            reverse=True)
        question = "{} {}".format(number_1, number_2)

        # more: https://en.wikipedia.org/wiki/Euclidean_algorithm
        def gcd_Euclidean(number_1, number_2):
            # q_n1 = number_1 // number_2 -- is not nessesary
            r_n1 = number_1 % number_2
            if r_n1 == 0:
                return number_2
            return gcd_Euclidean(number_2, r_n1)

        right_answer = gcd_Euclidean(number_1, number_2)
        right_answer = str(right_answer)

        return question, right_answer

    return DESCRIPTION, task_generator


def generator_brain_progression():
    # -- Description
    DESCRIPTION = ("{blue}═══ BRAIN PROGRESSION ═══{end}\n\n"
                   "  - What number is missing in the "
                   "progression?")
    DESCRIPTION = hf.colorize_string(DESCRIPTION)

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

    return DESCRIPTION, task_generator


def generator_brain_prime():
    # -- Description
    DESCRIPTION = ("{blue}═══ BRAIN PROGRESSION ═══{end}\n\n"
                   "  - Answer '{green}yes{end}' if given "
                   "number is prime. "
                   "Otherwise answer '{green}no{end}'.")
    DESCRIPTION = hf.colorize_string(DESCRIPTION)

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

    return DESCRIPTION, task_generator


def get_game(game):

    if game == "brain_even":
        return generator_brain_even()

    elif game == "brain_calc":
        return generator_brain_calc()

    elif game == "brain_gcd":
        return generator_brain_gcd()

    elif game == "brain_progression":
        return generator_brain_progression()

    elif game == "brain_prime":
        return generator_brain_prime()

    else:
        return None, None
