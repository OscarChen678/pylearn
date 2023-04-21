"""
File: PotholeFilling.py
Name: Oscar Chen
"""

from karel.stanfordkarel import *


def tR():
    turn_left()
    turn_left()
    turn_left()


def tL():
    turn_left()



def ith():
    tR()
    move()



def ofh():
    tL()
    tL()
    move()
    tR()


def p99():
    for i in range(99):
        put_beeper()

def main():
    for i in range(3):
        move()
        ith()
        p99()
        ofh()
        move()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
