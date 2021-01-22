"""This package use structure:
    1. 'scripts' - the package to call games
    2. 'games' - the package that contains rules
       of games (description, parameters and task generator)
    3. 'cli' - the module that creates command line interface
    4. 'engine' - the module that create basic mechanics of games.
       At the start game welcomes User and ask his name.
       Then engine shows to him description of current game and first question.
       For win User must give right answers for 3 questions.
       If any answer is wrong - User lost.

How it works:
    * Script [1] loads respective game rules [2] and engine [4]
    * Engine [4] takes game rules [2] and load command line interface [3]
"""
