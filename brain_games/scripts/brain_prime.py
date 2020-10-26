#!/usr/bin/env python3
import brain_games.scripts.cli_game_logics as cli


def main():
    cli.start_game(game_type="brain_prime", direct_call=True)


if __name__ == "__main__":
    main()
