#!/usr/bin/env python3
"""
Start the game 'brain prime'
"""

from brain_games import engine
from brain_games.games import prime


def main():
    engine.play(game=prime)


if __name__ == "__main__":
    main()
