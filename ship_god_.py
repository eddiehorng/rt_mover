#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

if __name__ == '__main__':
    game_name='god'
    startapp_and_go_compmode(1100, 360, game_name, 5)
    # for x in range(3, 4):
    #     swipe(600, 400, 800, 400, 2)
    #     click(185+x*320, 600, 6)
    #     click(640, 40, 8)
    for _ in range(0, 1):
        swipe(600, 400, 800, 400, 2)
        click(1145, 600, 8)

    game_name='stone_bless'
    # startapp_and_go_compmode(135, 360, game_name, 10)
    # for x in range(3, 4):
    #     swipe(600, 400, 800, 400, 2)
    #     click(185+x*320, 600, 6)
    #     click(640, 40, 8)

    # base construct resource
    startapp_and_go_compmode(1125, 360, 'base construct', 0)
    for _ in range(0, 1):
        swipe(600, 400, 800, 400, 2)
        click(1145, 600, 8)

    # ship resource
    startapp_and_go_compmode(930, 360, 'ship resource', 2)
    for _ in range(0, 1):
        swipe(600, 400, 800, 400, 2)
        click(1145, 600, 8)

    # 裝備副本
    startapp_and_go_compmode(1000, 360, 'gear-sub', 12, debug_no_start_app=1)
    for x in range(4):
        swipe(600, 400, 800, 400, 2)
        click(45+x*320, 600, 6)
        click(640, 40, 8)

    # 覺醒副本
    startapp_and_go_compmode(720, 360, 'wakeup-sub', 12, debug_no_start_app=1)
    # 初級
    click(180, 180, 2)
    click(1100, 690, 90)
    click(960, 400, 8)
    # 高級
    click(180, 310, 2)
    click(1100, 690, 90)
    click(960, 400, 8)
    # 王者級
    click(180, 380, 2)
    click(1100, 690, 90)
    click(960, 400, 8)