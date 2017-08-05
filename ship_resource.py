#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

do_enter_game=1
num_match=16

if __name__ == '__main__':
    if do_enter_game:
        enter_game()
    else:
        # back to main screen
        click(1215, 72, 2)
        click(1215, 72, 2)
        click(1215, 72, 2)

    #shop
    click(1090, 450, 1, hint='shop')
    click(960, 680, 2, hint='enter button')
    click(215, 200, 2, hint='black market')
    click(600, 270, 1)
    click(600, 445, 1)
    click(1020, 270, 1)
    click(1020, 445, 1)
    click(1215, 72, 2, 'back to main screen')

    swipe(300, 250, 900, 250, 2)
    click(690, 540, 1, hint='resource dust')
    click(470, 340, 1, hint='resource iron')
    click(200, 400, 1, hint='resource part')
    click(115, 270, 1, hint='resource yellow')
    click(400, 160, 1, hint='resource money')



