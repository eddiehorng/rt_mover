#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from utils import *
from ship_common import *

do_enter_game=1
num_match=40

def local_enter_game():
    if do_enter_game:
        enter_game()
    else:
        # back to main screen
        click(1215, 72, 2)
        click(1215, 72, 2)
        click(1215, 72, 2)

def enter_game_and_drink():
    local_enter_game()

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

    #friend
    local_enter_game()
    click(1090, 680, 1, hint='more')
    click(905, 570, 1, hint='friend')
    click(1073, 660, 1, hint='give')
    click(400, 660, 1, hint='get')

    # 任務
    local_enter_game()
    click(1225, 200, 2, hint='mission')
    for _ in range(6):
        click(1100, 230, 2, hint='get')

    # donate
    dn = [4, 4, 5, 3, 3]
    local_enter_game()
    click(860, 680, 2, hint='enter team')
    click(380, 630, 1, hint='donate')
    click(1050, 230, 1, 'donate 1st')
    xx = 280
    dx = 180
    for x2 in range(0, 5):
        for _ in range(0, dn[x2]):
            click(xx+x2*dx, 530, 0)

    # free get generel
    local_enter_game()
    click(445, 255, 2, hint='enter scheel')
    click(970, 690, 2, hint='enter button')
    click_on('free2', shift_x=0, shift_y=50, sleep_time=2, maxVal=0.95)
    click(1150, 300, 1, hint='any')
    click(200, 200, 2, hint='sea member')
    click_on('free3', shift_x=0, shift_y=0, sleep_time=1, maxVal=0.95)
    click(400, 340, 1, hint='1')
    click(650, 340, 1, hint='1')
    click(900, 340, 1, hint='1')
    click(400, 645, 1, hint='1')
    click(650, 645, 1, hint='1')
    click(900, 645, 1, hint='1')

    #advanced war
    # local_enter_game()
    # # enter battle
    # click(1233, 550, 6)
    # click(60, 230, 1, hint='adv')
    #
    # # fight
    # #for x, y in ((1100, 680), (1100, 330), (1100, 40)):
    # # for x, y in ((1100, 680), (1100, 330)): #, (1100, 40)):
    # #     click(x, y, 1)
    #
    # click(500, 550, 3, hint='enter war')
    # click(750, 335, 1, hint='5')
    # for _ in range(0, 5):
    #     click(200, 670, 3)
    #     click(500, 500, 2)
    # click(220, 120, 3, hint='world map')

if __name__ == '__main__':
    enter_game_and_drink()

    go_home()