#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

do_enter_game=1
num_match=40

def enter_game_and_drink():
    if do_enter_game:
        enter_game()
    else:
        # back to main screen
        click(1215, 72, 2)
        click(1215, 72, 2)
        click(1215, 72, 2)

    # drink
    click(1110, 200, 4)
    click(680, 640, 2)
    click(1215, 72,21)

if __name__ == '__main__':
    enter_game_and_drink()

