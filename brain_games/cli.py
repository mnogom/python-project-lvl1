import prompt

from brain_games import help_functions


def welcome_user():
    HEAD = ("{red}"
            "╔═══════════════════════════════════╗\n"
            "║   ╷                               ║\n"
            "║   ├─┐┌─┌─┐╷┌─┐  ┌─┐┌─┐┌┬┐┌─┐╶─╴   ║\n"
            "║   └─┘╵ └─┴╵╵ ╵  └─┤└─┴╵ ╵└─╴╶─╴   ║\n"
            "║                 ╶─┘               ║\n"
            "╚═══════════════════════════════════╝{end}\n\n"
            "  - Welcome to the Brain Games!\n  - What's your name?\n")
    HEAD = help_functions.colorize_string(HEAD)
    print(HEAD)

    username = get_user_answer()
    print("  - Hello, {}\n".format(username))

    return username


def get_user_answer():
    INPUT_SYMBOL = "{green}>>{end} "
    INPUT_SYMBOL = help_functions.colorize_string(INPUT_SYMBOL)

    try:
        answer = prompt.string(INPUT_SYMBOL)

    except KeyboardInterrupt:
        goodbye_user()

    if answer == "exit":
        goodbye_user()

    return answer


def goodbye_user():
    print("  - Gg! See you next time")
    exit()
