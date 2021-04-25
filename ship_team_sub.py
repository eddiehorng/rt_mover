#!/usr/bin/python
import datetime
from utils import *
from ship_common import *
from ship_drink_wine import enter_game_and_drink



if __name__ == '__main__':
    enter_game()

    click(860, 680, 2, hint='enter team')
    click(1085, 630, 3, hint='sub')

    for _ in range(8):
        for _ in range(6):
            if click_on('teamsub_box', sleep_time=1, maxVal=0.98):
                click(925, 300, sleep_time=1)
                click(925, 300, sleep_time=1)
                click(1060, 55, sleep_time=1, hint='X')
                click(1060, 110, sleep_time=1, hint='X')
            else:
                continue
        swipe(770, 100, 350, 100)

