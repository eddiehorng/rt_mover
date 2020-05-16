#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from utils import *
from ship_common import *


def temple():
    enter_game()

    # now = datetime.datetime.now()
    # time.sleep(now.hour*5)

    # 聖堂
    click(1090, 680, 1, hint='more')
    click(500, 570, 1, hint='聖堂')

    # swipe(500, 500, 500, 250, 1)
    # swipe(500, 500, 500, 250, 1)
    # swipe(500, 500, 500, 250, 1)
    # # click(215, 400, 3, hint='橫排轟炸')
    # click(320, 610, 3, hint='群體射擊')

    # click(190, 400, 3, hint='攻擊強化III')
    # click(290, 545, 3, hint='攻擊強化IV')

    # swipe(500, 500, 500, 250, 1)
    # click(740, 410, 3, hint='命中強化III')

    click(640, 675, 1, hint='特殊技巧')
    # swipe(500, 500, 500, 250, 1)
    # swipe(500, 500, 500, 250, 1)
    # click(615, 600, 2, hint='無情打擊')
    # click(650, 450, 2, hint='戰略掩護')
    # click(360, 565, 2, hint='閃避強化II')

    # click(1080, 675, 1, hint='防禦技巧')

    # swipe(500, 500, 500, 250, 1)
    # swipe(500, 500, 500, 250, 1)
    # click(500, 570-45, 1, hint='抗暴強化III')
    # click(320, 250, 1, hint='裝甲強化III')

    # swipe(500, 500, 500, 250, 1)
    # swipe(500, 500, 500, 250, 1)
    # swipe(500, 500, 500, 250, 1)
    # click(320, 610, 1, hint='閃避強化V')

    # click(210, 600, 1, hint='閃避強化IV')

    # click(510, 300, 1, hint='護盾強化II')
    # click(190, 400, 1, hint='護盾強化IV')
    # click(290, 600, 1, hint='閃避強化I')

    click(650, 300, 1, hint='憤怒出擊')
    # click(850, 350, 1, hint='窮追猛打')
    # click(800, 550, 1, hint='臨終X敵')

    click(780, 575, 1, hint='領悟')
    click(900, 450, 1, hint='確定')

    # in case need diamon
    # click(500, 560, 1, hint=u'取消')


if __name__ == '__main__':
    temple()

