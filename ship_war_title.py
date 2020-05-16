#!/usr/bin/python
import datetime
from utils import *
from ship_common import *


def prey():
    if click_on('alliance', shift_x=350, shift_y=-10, sleep_time=30, maxVal=0.97):
        click(500,300, hint='any', sleep_time=10)
        return True
    return False


if __name__ == '__main__':
    game_name='war-title'
    startapp_and_go_compmode(480, 360, game_name, 5)

    preied = 0
    for _ in range(120):
        if prey():
            preied += 1
            if preied >= 18:
                break
        else:
            click(1090, 680, hint='spend 1000, change')

