#!/usr/bin/env python3
"""Start the game 'brain progression'."""

from brain_games import engine
from brain_games.games import progression


def main():
    engine.play(game=progression)


if __name__ == "__main__":
    main()
