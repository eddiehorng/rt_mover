#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

do_enter_game=False

ntimes = 50
dn = [1, 3, 4, 3, 3]

def party_party():
    normal_wait = 0.3
    # create
    click(200, 220, normal_wait)
    # create 2
    click(730, 625, 1)
    # donate
    click(370, 625, normal_wait)
    # donate 1st
    click(1050, 230, normal_wait)

    xx = 280
    dx = 180
    # #1
    #click(xx, 530, 0)
    # #2
    for x2 in range(0, 5):
        for _ in range(0, dn[x2]):
            click(xx+x2*dx, 530, 0)

    # X
    click(1070, 111, normal_wait)
    # X
    click(1131, 65, normal_wait)
    # dismiss
    click(570, 340, normal_wait)
    # confirm
    click(640, 510, normal_wait)
    # any key
    click(640, 510, normal_wait)


if __name__ == '__main__':
    if do_enter_game:
        enter_game()

    # unity
    click(850, 680, 0.5)

    for i in range(0, ntimes):
        print '#{} round ...'.format(i)
        party_party()



