#!/usr/bin/python
import sys
from utils import *

start_loc=[[177,415],[525,529],[180,787],[512,970]]

appname='com.chengyou.ltjd.tw'
#'com.senjiahk.fleet'


def enter_game():
    startapp(appname, 40)
    for _ in range(0, 3):
        click(630, 680, 2, hint='close info')
    # click(1050, 665, 1, hint='switch account')
    # click(780, 610, 1, hint='login by account')
    # click(640, 515, 1, hint='account')
    # input_text(username, sleep_time=1)
    # click(630, 300, 1, hint='any')
    # click(500, 665, 1, hint='login')
    click(630, 600, 20, hint='enter game')  # enter game




def startapp_and_go_compmode(px, py, hint, swipe_times, debug_no_start_app=False):
    if not debug_no_start_app:
        enter_game()
    #if not click_on('ccenter', 20, retry=20): return False
    click(700, 500, 2, hint='ccenter') # c-center
    #if not click_on('enter', 1, retry=20): return False
    click(960, 680, 2, hint='enter button') # enter
    for i in range(0, swipe_times):
        swipe(800, 300, 500, 300, 2)
    click(px, py, 2, hint=hint)
    return True




