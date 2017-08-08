#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

if __name__ == '__main__':
    game_name='god'
    startapp_and_go_compmode(1000, 360, game_name, 5)
    for x in range(0, 4):
        swipe(600, 400, 800, 400, 2)
        click(230+x*320, 600, 6)
        click(640, 40, 8)

    # base construct resource
    startapp_and_go_compmode(1125, 360, game_name, 0)
    for _ in range(0, 2):
        swipe(600, 400, 800, 400, 2)
        click(1145, 600, 8)

    # ship resource
    startapp_and_go_compmode(1000, 360, game_name, 1)
    for _ in range(0, 2):
        swipe(600, 400, 800, 400, 2)
        click(1145, 600, 8)
