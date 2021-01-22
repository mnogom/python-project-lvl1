#!/usr/bin/env python3
"""Start the game 'brain gcd'."""

from brain_games import engine
from brain_games.games import gcd


def main():
    engine.play(game=gcd)


if __name__ == "__main__":
    main()
