#!/usr/bin/python
import datetime
from utils import *
from ship_common import *




if __name__ == '__main__':
    startapp_and_go_compmode(1100, 260, 'resource-war', 14, debug_no_start_app=0)

    # store
    click(1100, 590, sleep_time=2, hint='store')
    click(590, 250, sleep_time=2, hint='buy left-top')
    for _ in range(0, 2):
        click_on('mr_lo', shift_x=200, shift_y=50, sleep_time=1, maxVal=0.99)
        click_on('org_power', shift_x=0, shift_y=110, sleep_time=1, maxVal=0.99)
        click_on('soldier_food', shift_x=0, shift_y=110, sleep_time=1, maxVal=0.98)
    click_on('close_win2', sleep_time=1, maxVal=0.99)


    for island_n in [2, 2]:
        # in case leaved, enter resource-war again
        click(1100, 260, sleep_time=2)
        for _ in range(island_n):
            click(788, 670, sleep_time=1)

        # swipe to right most
        for _ in range(3):
            swipe(800, 300, 350, 300, 2)

        click(950, 350, sleep_time=1)
        click(880, 625, sleep_time=60, hint='attack')
        click(500, 500, sleep_time=10, hint='any')
        # in case of already occupired 2 islands
        click_on('close_win2', sleep_time=1, maxVal=0.99)
        click_on('close_win2', sleep_time=1, maxVal=0.99)
        # click(940, 270, sleep_time=1, hint='X')
        # click(1140, 70, sleep_time=1, hint='X')



