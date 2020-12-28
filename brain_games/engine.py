import prompt

from brain_games import cli


COUNT_OF_ANSWERS_TO_WIN = 3
TEMPLATE_QUESTION = "Question: {task}"
TEMPLATE_ON_RIGHT_ANSWER = "Correct!"
TEMPLATE_ON_WRONG_ANSWER = ("'{user_answer}' is wrong answer ;(. "
                            "Correct answer was '{right_answer}'.\n"
                            "Let's try again, {username}!")
TEMPLATE_ON_WIN = "Congratulations, {username}!"


def play(game):
    username = cli.welcome_user()

    # -- Init game: counter of correct answers
    correct_answers = 0

    # -- Show to user Description
    print(game.DESCRIPTION)

    # -- Main game mechanic
    while correct_answers < COUNT_OF_ANSWERS_TO_WIN:

        game_task, game_answer = game.generate_task()
        print(TEMPLATE_QUESTION.format(task=game_task))
        user_answer = prompt.string("Your answer: ")

        if user_answer == game_answer:
            correct_answers += 1
            print(TEMPLATE_ON_RIGHT_ANSWER)

        else:
            print(TEMPLATE_ON_WRONG_ANSWER.format(
                username=username,
                user_answer=user_answer,
                right_answer=game_answer))
            break

    else:
        print(TEMPLATE_ON_WIN.format(username=username))
