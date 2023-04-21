"""
File: DoubleBeepers.py
Name: Oscar Chen
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
    move()
    while on_beeper():
        pick_beeper()
        turn_left()
        turn_left()
        move()
        put_beeper()
        turn_left()
        turn_left()
        move()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
