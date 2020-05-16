#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

if __name__ == '__main__':
    enter_game()
    #shop
    click(1090, 450, 1, hint='shop')
    click(960, 680, 2, hint='enter button')
    for _ in range(0, 6):
        click_on('free1', sleep_time=2, maxVal=0.96)



