#!/usr/bin/python
import datetime
from utils import *
from ship_common import *
from ship_drink_wine import enter_game_and_drink

num_match=25

if __name__ == '__main__':
    enter_game_and_drink()

    #buy power
    # click(45, 60, 2)
    # click(999, 210, 1, hint='buy button')
    # for _ in range(0, 3):
    #     click(640, 600, 1, hint='diamon')
    #     click(1215, 72, 2)
    # click(850, 215, 1, hint='close')
    # click(1215, 72, 2)

    # enter battle
    click(1233, 550, 6)
    click(500, 550, 3)

    # fight
    for _ in range(0, num_match):
        for _ in range(0, 3):
            click(200, 670, 3)
            click(500, 500, 2)
        swipe(100, 600, 500, 500, 2)



