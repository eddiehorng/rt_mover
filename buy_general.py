#!/usr/bin/python
import datetime
from utils import *
from ship_common import *
from ship_drink_wine import enter_game_and_drink

ntimes = int(os.environ.get('ntimes', 250))

if __name__ == '__main__':
    for _ in range(0, ntimes):
        click(400, 320, 13, hint='3000')
        click(700, 550, 1, hint='general')
        click(800, 500, 1, hint='cancel')
        # click(840, 210, 1, hint='any')


    go_home()