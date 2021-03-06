#!/usr/bin/env python3
"""Start the game 'brain even'."""

from brain_games import engine
from brain_games.games import even


def main():
    engine.play(game=even)


if __name__ == "__main__":
    main()
