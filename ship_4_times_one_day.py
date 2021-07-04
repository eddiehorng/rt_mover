#!/usr/bin/python
import datetime
from utils import *
from ship_common import *


if __name__ == '__main__':
    enter_game()

    click(860, 680, 2, hint='enter team')
    click(660, 630, 2, hint='team store')
    click(600, 245, 2, hint='upper-left')
    click_on('close_win2', sleep_time=2, maxVal=0.99)
    click_on('close_win2', sleep_time=2, maxVal=0.99)
    click_on('close_win2', sleep_time=2, maxVal=0.99)

    click(445, 255, 2, hint='enter scheel')
    click(970, 690, 2, hint='enter button')
    click(210, 280, 2, hint='scheel store')
    for _ in range(0, 4):
        # if not click_on('war_coin', sleep_time=2, maxVal=0.95):
        click_on('peice', shift_x=-100, shift_y=100, sleep_time=2, maxVal=0.95)
        click_on('org_power', shift_x=-60, shift_y=100, sleep_time=2, maxVal=0.95)
        click(1150, 300, 1, hint='any')
    click_on('close_win2', sleep_time=2, maxVal=0.99)
    click_on('close_win2', sleep_time=2, maxVal=0.99)

    go_home()
