#!/usr/bin/env python3
"""Start the game 'brain calc'."""

from brain_games import engine
from brain_games.games import calc


def main():
    engine.play(game=calc)


if __name__ == "__main__":
    main()
