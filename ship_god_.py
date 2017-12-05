#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

if __name__ == '__main__':
    game_name='god'
    startapp_and_go_compmode(1100, 360, game_name, 5)
    for x in range(0, 4):
        swipe(600, 400, 800, 400, 2)
        click(185+x*320, 600, 6)
        click(640, 40, 8)

    game_name='stone_bless'
    startapp_and_go_compmode(135, 360, game_name, 10)
    for x in range(0, 4):
        swipe(600, 400, 800, 400, 2)
        click(185+x*320, 600, 6)
        click(640, 40, 8)

    # base construct resource
    startapp_and_go_compmode(1125, 360, game_name, 0)
    for _ in range(0, 2):
        swipe(600, 400, 800, 400, 2)
        click(1145, 600, 8)

    # ship resource
    startapp_and_go_compmode(930, 360, game_name, 2)
    for _ in range(0, 2):
        swipe(600, 400, 800, 400, 2)
        click(1145, 600, 8)