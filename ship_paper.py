#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

fight_loc=[(290, 250), (640, 250), (990, 250), (290, 460), (640, 460), (990, 460)]
draw_loc=[(200, 320), (375, 320), (550, 320), (725, 320), (900, 320), (1080, 320)]

def paper_fight(n):
    click(fight_loc[n][0], fight_loc[n][1], 1)
    if not click_on('clear_fight', 8): return False
    if not click_on('close_win', 1, maxVal=0.99): return False
    if not click_on('close_win', 1, maxVal=0.99): return False
    return True


def do_paper_fight():
    for n in range(0, len(fight_loc)):
        if not paper_fight(n):
            # try to go back init screen
            for _ in range(0, 3):
                click(636, 40, 0.5)
            if not click_on('ship_fac_title', maxVal=0.999):
                log('Failed to do ship fight %d'%n)
                break

def free_paper(n):
    click(draw_loc[n][0], draw_loc[n][1], 3)
    click_on('free_paper2', 30, maxVal=0.997)
    click_on('free_paper', 30)
    click(630, 40, 1)
    click(630, 40, 1)

def do_draw_paper():
    if click_on('draw_paper',3):
        for n in range(0, len(draw_loc)):
            free_paper(n)


if __name__ == '__main__':
    game_name='ship_factory'

    for _ in range(3):
        if not startapp_and_go_compmode(game_name, 0, debug_no_start_app=False):
            log('Failed to enter %s' % game_name)
            sys.exit(0)
        do_draw_paper()

    if not startapp_and_go_compmode(game_name, 0, debug_no_start_app=False):
        log('Failed to enter %s' % game_name)
        sys.exit(0)
    do_paper_fight()





