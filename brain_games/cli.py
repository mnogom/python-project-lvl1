from typing import Optional
import prompt


HEAD = ("{red}"
        "╔═══════════════════════════════════╗\n"
        "║   ╷                               ║\n"
        "║   ├─┐┌─┌─┐╷┌─┐  ┌─┐┌─┐┌┬┐┌─┐╶─╴   ║\n"
        "║   └─┘╵ └─┴╵╵ ╵  └─┤└─┴╵ ╵└─╴╶─╴   ║\n"
        "║                 ╶─┘               ║\n"
        "╚═══════════════════════════════════╝{end}\n")
INPUT_SYMBOL = "{green}>>{end} "


def _format(text: str, **kwargs) -> str:
    """
    Function returns formatted text with bash colors codes.
    Use {red}, {green} or {blue}. End of color string - {end}

    :param text: text to color
    :return: colorized string
    """
    return text.format(
        red="\033[31m",
        green="\033[32m",
        blue="\033[94m",
        end="\033[0m",
        **kwargs
    )


def render_text(text: str, **kwargs) -> None:
    """
    Function to print string for user

    :param text: text to print
    """
    print(_format(text, **kwargs))


def get_user_answer(question=None, **kwargs) -> Optional[str]:
    """
    Function to get user answer. If user print "exit" or use
    "Keyboard interrupt" function returns None. Also you can
    send question that will print before row with input

    :param question: render "question" before input
    :return: username or None
    """
    if question is not None:
        render_text(question, **kwargs)

    try:
        answer = prompt.string(_format(INPUT_SYMBOL))

    except KeyboardInterrupt:
        return None

    if answer == "exit":
        return None

    return answer


def welcome_user() -> str:
    """
    Greeting function

    :return: username
    """
    render_text(HEAD)
    render_text("  - Welcome to the Brain Games!")
    username = get_user_answer("  - What's your name?")

    if username is not None:
        render_text("  - Hello, {username}\n", username=username)

    return username


def goodbye_user() -> None:
    """
    Function for exit

    :return: None
    """
    render_text("  - See you next time")
    exit()
