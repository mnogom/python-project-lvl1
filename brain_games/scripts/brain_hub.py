import brain_games.scripts.cli_game_logics as cli


def load_game(username, game):
    result = cli.start_game(
        game_type=game,
        direct_call=False,
        username=username)

    print(result)


def user_exit(username):
    print("Gg, {}. See you next time!".format(username))


def choose_game(username, games):
    color_green = "\033[32m"
    color_end = "\033[0m"
    print("{}, choose Game".format(username))
    for key, value in games.items():
        print("  [{green}{i}{end}]: {name}".format(
            green=color_green,
            end=color_end,
            i=key,
            name=value.replace("_", " ")))
    answer = cli.get_user_answer()
    if answer in games.keys():
        return games[answer]
    else:
        return None


def main():
    # -- Some info
    games = {
        "1": "brain_even",
        "2": "brain_calc",
        "3": "brain_gcd",
        "4": "brain_progression",
        "5": "brain_prime"
    }
    game_active = True
    # -- Greetings
    username = cli.welcome_user()
    # -- Infinity train
    while game_active:
        game = choose_game(username, games)
        if game:
            load_game(username, game)
        else:
            game_active = False

    user_exit(username)


if __name__ == "__main__":
    main()
