from brain_games import cli


COUNT_OF_ANSWERS_TO_WIN = 3
TEMPLATE_QUESTION = "  - Question: {task}"
TEMPLATE_ON_RIGHT_ANSWER = "  - {green}Correct!{end}\n"
TEMPLATE_ON_WRONG_ANSWER = ("  - {red}{user_answer}{end} is wrong answer ;(."
                            "Correct answer was {green}{right_answer}{end}.\n"
                            "  - Let's try again, {username}!\n")
TEMPLATE_ON_WIN = "  - Congratulations, {username}! You win!"


def want_exit(answer: str) -> bool:
    """
    Predicate to check if user don't want to play

    :param answer: user answer
    :return: flag True if user want to exit
    """
    return True if answer is None or answer == "exit" else False


def play(game):
    """
    Play game. Game must be package with 'DESCRIPTION' and
    function 'generate_task()' that returns question[str] and right_answer[str]

    :param game: core of game
    :return: None
    """
    username = cli.welcome_user()
    if want_exit(username):
        cli.goodbye_user()
        return

    # -- Init game: counter of correct answers
    correct_answers = 0

    # -- Show to user Description
    cli.render_text(game.DESCRIPTION)

    # -- Main game mechanic
    while correct_answers < COUNT_OF_ANSWERS_TO_WIN:

        game_task, game_answer = game.generate_task()
        user_answer = cli.get_user_answer(TEMPLATE_QUESTION, task=game_task)

        if want_exit(user_answer):
            break

        elif user_answer == game_answer:
            correct_answers += 1
            cli.render_text(TEMPLATE_ON_RIGHT_ANSWER)

        else:
            cli.render_text(TEMPLATE_ON_WRONG_ANSWER,
                            username=username,
                            user_answer=user_answer,
                            right_answer=game_answer)
            break

    else:
        cli.render_text(TEMPLATE_ON_WIN, username=username)

    cli.goodbye_user()
    return
