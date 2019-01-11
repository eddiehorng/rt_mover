#!/usr/bin/python
import datetime
from utils import *
from ship_common import *
from ship_drink_wine import enter_game_and_drink


if __name__ == '__main__':
    enter_game()

    click(860, 680, 2, hint='enter team')
    click(955, 630, 5, hint='team war-cross server')

    click(1055, 700, 2, hint='store')
    for _ in range(0, 12):
        click(600, 640, 1, hint='soldier')

    swipe(500, 600, 500, 300, 2)
    for _ in range(0, 5):
        click(600, 670, 1, hint='equipment box')