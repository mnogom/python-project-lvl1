#!/usr/bin/env python3
import brain_games.scripts.cli_game_logics as cli


def main():
    username = cli.welcome_user()
    cli.start_even_game(username)


if __name__ == "__main__":
    main()
