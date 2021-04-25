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


    # for _ in range(0, 8):
    #     click(600, 450, 3, hint='big treasure box')

    for _ in range(0, 20):
        click(600, 640, 3, hint='soldier')

    swipe(500, 600, 500, 300, 2)
    for _ in range(0, 9):
        click(600, 670, 3, hint='equipment box')