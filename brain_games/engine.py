"""Module create templates for game status and describe engine of any game."""

import prompt


COUNT_OF_ROUNDS_TO_WIN = 3

TEMPLATE_QUESTION = "Question: {task}"
TEMPLATE_ON_RIGHT_ANSWER = "Correct!"
TEMPLATE_ON_WRONG_ANSWER = ("'{user_answer}' is wrong answer ;(. "
                            "Correct answer was '{right_answer}'.\n"
                            "Let's try again, {username}!")
TEMPLATE_ON_WIN = "Congratulations, {username}!"
TEMPLATE_WELCOME = "Welcome to the Brain Games!"
TEMPLATE_GREETING = "Hello, {}!"
TEMPLATE_GET_NAME = "May I have your name? "
TEMPLATE_GET_ANSWER = "Your answer: "


def play(game) -> None:
    """Main function to start the game.

    At the start game welcomes User and ask his name.
    Then engine shows to him description of current game and first question.
    For win User must give right answers for 3 questions.
    If any answer is wrong - User lost.

    :param game: module with game rules. Module must contain DESCRIPTION and
    function generate_task (that must return the question and the right answer)
    """

    print(TEMPLATE_WELCOME)
    username = prompt.string(TEMPLATE_GET_NAME)
    print(TEMPLATE_GREETING.format(username))

    # -- Show to user Description
    print(game.DESCRIPTION)

    # -- Main game mechanic
    for _ in range(COUNT_OF_ROUNDS_TO_WIN):

        game_question, right_answer = game.generate_round()
        print(TEMPLATE_QUESTION.format(task=game_question))
        user_answer = prompt.string(TEMPLATE_GET_ANSWER)

        if user_answer != right_answer:
            print(TEMPLATE_ON_WRONG_ANSWER.format(
                username=username,
                user_answer=user_answer,
                right_answer=right_answer))
            return

        print(TEMPLATE_ON_RIGHT_ANSWER)

    print(TEMPLATE_ON_WIN.format(username=username))
