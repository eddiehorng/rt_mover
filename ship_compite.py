#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

if __name__ == '__main__':
    game_name='ship_compite'
    startapp_and_go_compmode(280, 400, game_name, 0, debug_no_start_app=False)

    for _ in range(0, 5):
        click(1060, 580, 90, hint='challenge')
        click(1060, 580, 61*5)

    game_name='top_ship_compite'
    startapp_and_go_compmode(460, 400, game_name, 10, debug_no_start_app=False)

    for _ in range(0, 5):
        click(1060, 580, 90, hint='challenge')
        click(1060, 580, 61*5)




