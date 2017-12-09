#!/usr/bin/python
import datetime
from utils import *
from ship_common import *
from ship_drink_wine import enter_game_and_drink

if __name__ == '__main__':
    enter_game()

    click(860, 680, 2, hint='enter team')
    click(800, 630, 5, hint='team war')
    click(470, 310, 1, hint='#3')
    click(890, 460, 3, hint='button: check this team')

    click(1070, 720, 2, hint='button: next page')
    click(1070, 720, 2, hint='button: next page')
    click(1070, 720, 2, hint='button: next page')

    # fight
    click(1070, 320, 2, hint='select one match')
    #fight (not sure location correct)
    click(640, 660, 0)


