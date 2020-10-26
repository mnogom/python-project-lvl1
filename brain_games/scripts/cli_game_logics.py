import prompt
import random


def welcome_user():
    color_red = "\033[31m"
    color_green = "\033[32m"
    color_end = "\033[0m"
    head = """
    │
    ├─┐┌─┌─┐╷┌─┐  ┌─┐┌─┐┌┬┐┌─┐╶─╴
    └─┘╵ └─┴╵╵ ╵  └─┤└─┴╵ ╵└─╴╶─╴
                  ╶─┘
"""
    print("{red}{dashes}{head}{dashes}{end}".format(
        red=color_red,
        dashes="=" * 45,
        head=head,
        end=color_end))
    print("Welcome to the Brain Games!")
    username = prompt.string("What's your name? {green}>>{end} ".format(
        green=color_green,
        end=color_end))
    print("Hello, {}".format(username))

    return username


def start_even_game(username):
    color_red = "\033[31m"
    color_blue = "\033[94m"
    color_green = "\033[32m"
    color_end = "\033[0m"
    print("{blue}=== EVEN-MASTER ===.{end}\n\
Answer '{green}yes{end}' if the number is even,\
otherwise answer '{green}no{end}'.".format(
            blue=color_blue,
            green=color_green,
            end=color_end
        ))
    game_active = True
    correct_answers = 0
    while game_active:
        # Generate task and get user answer
        current_number = random.randint(0, 100)
        print("Question: {}".format(current_number))
        right_answer = "yes" if current_number % 2 == 0 else "no"
        user_answer = prompt.string("{green}>>{end} ".format(
            green=color_green,
            end=color_end))
        # Check answer
        if user_answer == right_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print("'{red}{user_answer}{end}' is wrong answer ;(.\
Correct answer was '{green}{right_answer}{end}'.\n\
Let's try again, {username}!".format(
                user_answer=user_answer,
                right_answer=right_answer,
                username=username,
                red=color_red,
                green=color_green,
                end=color_end))
            game_active = False
            return False
        if correct_answers == 3:
            print("Congratulations, {}!".format(username))
            return True
