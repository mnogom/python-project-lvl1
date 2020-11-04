#!/usr/bin/env python3
from brain_games import game_mechanic
from brain_games.games import brain_prime_core


def main():
    game_mechanic.start(
        game_description=brain_prime_core.DESCRIPTION,
        game_generator=brain_prime_core.task_generator
    )


if __name__ == "__main__":
    main()
