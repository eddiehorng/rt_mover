#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

num_match=14

if __name__ == '__main__':
    game_name='champ_game'
    if enter_game():
        log('Failed to enter game')
        sys.exit(1)

    # drink
    click(1110, 200, 2)
    click(680, 640, 1)

    # enter battle
    click(1233, 550, 3)
    click(500, 550, 1)

    # fight
    for _ in range(0, num_match):
        for _ in range(0, 3):
            click(200, 670, 2)
            click(500, 500, 1)
        swipe(100, 600, 500, 500, 1)



