#!/usr/bin/python
import datetime
from utils import *
from ship_common import *




if __name__ == '__main__':
    startapp_and_go_compmode(1000, 360, 'resource-war', 14, debug_no_start_app=0)

    for island_n in [1, 2]:
        for _ in range(island_n):
            click(788, 670, sleep_time=1)
        # swipe to left most
        for _ in range(3):
            swipe(800, 300, 350, 300, 2)
        click(920, 140, sleep_time=1)
        click(880, 650, sleep_time=60, hint='attack')
        # in case of already occupired 2 islands
        click(940, 270, sleep_time=1, hint='X')
        click(1140, 70, sleep_time=1, hint='X')



