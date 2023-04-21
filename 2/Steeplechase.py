"""
File: Steeplechase.py
Name: Oscar Chen
"""

from karel.stanfordkarel import *
def jp():
    while not front_is_clear():
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    while front_is_clear():
        move()
    while not front_is_clear():
        jp()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
