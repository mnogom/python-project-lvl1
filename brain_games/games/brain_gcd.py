#!/usr/bin/env python3
import brain_games.scripts.game_mechanic as game


def main():
    game.start(game_type="brain_gcd", direct_call=True)


if __name__ == "__main__":
    main()
