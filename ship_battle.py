#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

do_enter_game=0
num_match=16

if __name__ == '__main__':
    if do_enter_game:
        if enter_game():
            log('Failed to enter game')
            sys.exit(1)
        time.sleep(60)
    else:
        # back to main screen
        click(1215, 72, 2)
        click(1215, 72, 2)
        click(1215, 72, 2)

    # drink
    click(1110, 200, 4)
    click(680, 640, 2)
    click(1215, 72,21)

    # enter battle
    click(1233, 550, 6)
    click(500, 550, 3)

    # fight
    for _ in range(0, num_match):
        for _ in range(0, 3):
            click(200, 670, 3)
            click(500, 500, 2)
        swipe(100, 600, 500, 500, 2)



