from brain_games import help_functions
from brain_games.scripts import cli


def start(game_description, game_generator, username=None, direct_call=True):
    # -- Check if game started directly (True) or from HUB (False)
    if direct_call:
        username = cli.welcome_user()

    if username is None:
        # Need to check this
        raise NameError("Username is None. Try to check 'direct_call' value")

    # -- Init game: Description, Task Generator, Game status
    correct_answers = 0

    # -- Show to user Descriprtion
    print(game_description)

    # -- Main game mechanic
    while correct_answers < 3:

        game_task, game_answer = game_generator()
        print("  - Question: {}".format(game_task))
        user_answer = cli.get_user_answer()

        if user_answer == game_answer:
            correct_answers += 1
            print("  - Correct!\n")
        else:
            message = ("  - '{{red}}{user_answer}{{end}}' is wrong answer ;(."
                       "Correct answer was '{{green}}{right_answer}{{end}}'.\n"
                       "  - Let's try again, {username}!\n")
            message = message.format(
                user_answer=user_answer,
                right_answer=game_answer,
                username=username
            )
            message = help_functions.colorize_string(message)
            print(message)
            return False

    print("Congratulations, {}!".format(username))
    return True
