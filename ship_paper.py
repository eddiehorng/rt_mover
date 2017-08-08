#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

fight_loc=[(290, 250), (640, 250), (990, 250), (290, 460), (640, 460), (990, 460)]
draw_loc=[(200, 320), (375, 320), (550, 320), (725, 320), (900, 320), (1080, 320)]

def paper_fight(n):
    click(fight_loc[n][0], fight_loc[n][1], 1)
    click(815, 520, 8, hint='clear fight')
    click(1055, 130, 1, hint='close win')
    click(950, 80, 1, hint='leave')
    #if not click_on('clear_fight', 8): return False
    #if not click_on('close_win', 1, maxVal=0.99): return False
    #if not click_on('close_win', 1, maxVal=0.99): return False
    return True


def do_paper_fight():
    for n in range(0, len(fight_loc)):
        paper_fight(n)

def free_paper(n):
    click(draw_loc[n][0], draw_loc[n][1], 3)
    click(420, 630, 5, hint='free paper')
    click(630, 40, 1, hint='any')
    click(630, 40, 1, hint='any')
    click(420, 630, 5, hint='free paper')
    #click_on('free_paper2', 30, maxVal=0.997)
    #click_on('free_paper', 30)
    click(630, 40, 1)
    click(630, 40, 1)

def do_draw_paper():
    #if click_on('draw_paper',3):
    click(1055, 670, 3, hint='draw paper')
    for n in range(0, len(draw_loc)):
        free_paper(n)
        click(630, 40, 1, hint='any')
        click(630, 40, 1, hint='any')


if __name__ == '__main__':
    px, py = 600, 400
    game_name='ship_factory'

    startapp_and_go_compmode(px, py, game_name, 0, debug_no_start_app=False)
    do_draw_paper()

    startapp_and_go_compmode(px, py, game_name, 0, debug_no_start_app=False)
    do_paper_fight()





