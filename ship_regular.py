#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

do_enter_game=0
num_match=40

def enter_game_and_drink():
    if do_enter_game:
        enter_game()
    else:
        # back to main screen
        click(1215, 72, 2)
        click(1215, 72, 2)
        click(1215, 72, 2)

    click(1225, 450, 2, hint='active')
    # 7 days gift
    click(570, 370, 1, hint='get')
    click(570, 670, 1, hint='get')

    # everyday sign
    click(200, 260, 1, hint='enter every day sign')
    for x in range(0, 5):
        for y in range(0, 4):
            click(405+x*150, 185+y*150, 1, hint='array click')
            click(405, 185, 0.5)

    click(200, 110, 1)
    swipe(200, 680, 200, 100, 1)

    #spent $1000
    click(205, 310, 1, hint='so shu')
    click(1025, 170, 1, hint='get')

    #month card
    click(205, 610, 1, hint='month card')
    click(600, 610, 1, hint='get')



if __name__ == '__main__':
    enter_game_and_drink()

