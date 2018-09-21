#!/usr/bin/python
import datetime
from utils import *
from ship_common import *
from ship_drink_wine import enter_game_and_drink

def take_oil(island_x, islandy):
    click(island_x, islandy, 2, hint='enter island')
    for y in range(0, 6):
        for t in range(0, 5):
            click(1130, 110+y*65, 2, hint='take oild from someone')
            click(650, 460, 60, hint='take')
            click(650, 460, 12, hint='any, war over')

if __name__ == '__main__':
    # enter_game()

    # click(860, 680, 2, hint='enter team')
    # click(955, 630, 5, hint='team war-cross server')

    take_oil(900, 630)
