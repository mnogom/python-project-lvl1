def colorize_string(string):
    COLOR_RED = "\033[31m"
    COLOR_GREEN = "\033[32m"
    COLOR_BLUE = "\033[94m"
    COLOR_END = "\033[0m"
    return string.format(
        red=COLOR_RED,
        green=COLOR_GREEN,
        blue=COLOR_BLUE,
        end=COLOR_END
    )
