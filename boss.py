#!/usr/bin/python
from utils import *

boss_loc=[[177,415],[525,529],[180,787],[512,970]]

if __name__ == '__main__':
    startapp()
    click_on('enter', 3)
    click_on('boss', 2)
    for loc in boss_loc:
        click(loc[0], loc[1], 2)
        click(36, 594) # left arror
        if click_on('attack_b', 1) == -1: break
        if click_on('dialog_crop', 60) == -1: break
        click_on('gameover_crop', 2)
        click_on('continue_crop', 2)
        click_on('fail_continue', 2)
        click_on('return', 2)
