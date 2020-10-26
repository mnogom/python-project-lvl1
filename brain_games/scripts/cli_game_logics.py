import prompt
import random


def get_user_answer():
    color_green = "\033[32m"
    color_end = "\033[0m"
    answer = prompt.string("{green}>>{end} ".format(
        green=color_green,
        end=color_end))
    return answer


def welcome_user():
    color_red = "\033[31m"
    color_end = "\033[0m"
    head = """
    ╷
    ├─┐┌─┌─┐╷┌─┐  ┌─┐┌─┐┌┬┐┌─┐╶─╴
    └─┘╵ └─┴╵╵ ╵  └─┤└─┴╵ ╵└─╴╶─╴
                  ╶─┘
"""
    print("{red}{dashes}{head}{dashes}{end}".format(
        red=color_red,
        dashes="=" * 45,
        head=head,
        end=color_end))
    print("Welcome to the Brain Games!\nWhat's your name? ")
    username = get_user_answer()
    print("Hello, {}".format(username))
    return username


def get_game_mechanics(game_type, direct_call):
    """return game description"""
    color_blue = "\033[94m"
    color_green = "\033[32m"
    color_end = "\033[0m"
    # -- Game description
    brain_even_description = ("{blue}=== BRAIN EVEN ==={end}\n"
                              "Answer '{green}yes{end}' if the number is even,"
                              "otherwise answer '{green}no{end}'.").format(
                                  blue=color_blue,
                                  green=color_green,
                                  end=color_end)
    brain_calc_description = ("{blue}=== BRAIN CALC =={end}\n"
                              "What is the result of the expression?".format(
                                  blue=color_blue,
                                  end=color_end
                                ))
    brain_gcd_description = ("{blue}=== BRAIN GCD =={end}\n"
                             "Find the greatest common divisor"
                             "of given numbers.".format(
                                  blue=color_blue,
                                  end=color_end
                                ))

    # -- Task generators
    def brain_even_generator():
        # 'current_number' here is the question
        current_number = random.randint(0, 100)
        right_answer = "no" if current_number % 2 else "yes"
        return current_number, right_answer

    def brain_calc_generator():
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

    def brain_gcd_generator():
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

    # -- Returns
    if game_type == "brain_even":
        return (brain_even_description, brain_even_generator)
    elif game_type == "brain_calc":
        return (brain_calc_description, brain_calc_generator)
    elif game_type == "brain_gcd":
        return (brain_gcd_description, brain_gcd_generator)
    return None


def start_game(game_type, username=None, direct_call=True):
    # -- Some colors
    color_red = "\033[31m"
    color_green = "\033[32m"
    color_end = "\033[0m"
    # -- Check if game started directly (True) or from HUB (False)
    if direct_call:
        username = welcome_user()
    if username is None:
        # Need to check this
        raise NameError("Username is None. Try to check 'direct_call' value")
    # -- Init game: Description, Task Generator, Game status
    game_description, game_generator = get_game_mechanics(
        game_type,
        direct_call)
    correct_answers = 0
    # -- Show to user Descriprtion
    print(game_description)
    # -- Main game mechanic
    while correct_answers < 3:
        game_task, game_answer = game_generator()
        print("Question: {}".format(game_task))
        user_answer = get_user_answer()
        if user_answer == game_answer:
            correct_answers += 1
            print("Correct!")
        else:
            print(("'{red}{user_answer}{end}' is wrong answer ;(."
                   "Correct answer was '{green}{right_answer}{end}'.\n"
                   "Let's try again, {username}!").format(
                       user_answer=user_answer,
                       right_answer=game_answer,
                       username=username,
                       red=color_red,
                       green=color_green,
                       end=color_end))
            return False
    print("Congratulations, {}!".format(username))
    return True
