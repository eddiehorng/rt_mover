#!/usr/bin/python
import datetime
from utils import *

start_loc=[[177,415],[525,529],[180,787],[512,970]]

appname='com.chengyou.ltjd.tw'
#'com.senjiahk.fleet'

def enter_game():
    startapp(appname, 50)
    for _ in range(0, 5):
        if click_on('close_win', 2, maxVal=0.99): break
    click(630, 680, 1)
    click(630, 680, 1)
    click(630, 680, 1)
    if not click_on('enter_game', 20, maxVal=0.8, retry=5): return False

def startapp_and_go_compmode(comp_crop, swipe_times, debug_no_start_app=False):
    if not debug_no_start_app:
        enter_game()
        if not click_on('ccenter', 20, retry=20): return False
        if not click_on('enter', 1, retry=20): return False
        time.sleep(3)
        for i in range(0, swipe_times+1):
            if click_on(comp_crop, 1, maxVal=0.99): return True
            swipe(800, 250, 300, 300, 2)

    else:
        return True
    return False




