"""
File: StepUp.py
Name: Oscar Chen
"""

from karel.stanfordkarel import *
def tr():
    turn_left()
    turn_left()
    turn_left()

def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    tr()
    move()
    put_beeper()
    move()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
