import prompt
from brain_games.scripts.game_rules import get_game
import brain_games.scripts.help_functions as hf


def get_user_answer():
    INPUT_SYMBOL = "{green}>>{end} "
    INPUT_SYMBOL = hf.colorize_string(INPUT_SYMBOL)
    answer = prompt.string(INPUT_SYMBOL)
    return answer


def welcome_user():
    HEAD = ("{red}"
            "╔═══════════════════════════════════╗\n"
            "║   ╷                               ║\n"
            "║   ├─┐┌─┌─┐╷┌─┐  ┌─┐┌─┐┌┬┐┌─┐╶─╴   ║\n"
            "║   └─┘╵ └─┴╵╵ ╵  └─┤└─┴╵ ╵└─╴╶─╴   ║\n"
            "║                 ╶─┘               ║\n"
            "╚═══════════════════════════════════╝{end}\n\n"
            "  - Welcome to the Brain Games!\n  - What's your name?\n")
    HEAD = hf.colorize_string(HEAD)
    print(HEAD)
    username = get_user_answer()
    print("  - Hello, {}\n".format(username))
    return username


def start(game_type, username=None, direct_call=True):
    # -- Check if game started directly (True) or from HUB (False)
    if direct_call:
        username = welcome_user()
    if username is None:
        # Need to check this
        raise NameError("Username is None. Try to check 'direct_call' value")
    # -- Init game: Description, Task Generator, Game status
    game_description, game_generator = get_game(game_type)
    correct_answers = 0
    # -- Show to user Descriprtion
    print(game_description)
    # -- Main game mechanic
    while correct_answers < 3:
        game_task, game_answer = game_generator()
        print("  - Question: {}".format(game_task))
        user_answer = get_user_answer()
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
            message = hf.colorize_string(message)
            print(message)
            return False
    print("Congratulations, {}!".format(username))
    return True
