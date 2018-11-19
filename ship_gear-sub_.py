#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from utils import *
from ship_common import *

if __name__ == '__main__':
    # 裝備副本
    startapp_and_go_compmode(1000, 360, 'gear-sub', 12, debug_no_start_app=0)
    for x in range(4):
        swipe(600, 400, 800, 400, 2)
        click(230+x*320, 600, 10)
        click(640, 40, 8)

    # 覺醒副本
    startapp_and_go_compmode(720, 360, 'wakeup-sub', 12, debug_no_start_app=0)
    # 初級
    click(180, 180, 2)
    click(1140, 670, 90)
    click(960, 400, 8)
    # 高級
    click(180, 310, 2)
    click(1140, 670, 90)
    click(960, 400, 8)
    # 王者級
    click(180, 380, 2)
    click(1140, 670, 90)
    click(960, 400, 8)