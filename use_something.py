#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

do_enter_game=False

ntimes = 470


if __name__ == '__main__':
    for i in range(0, ntimes):
        print '#{} round ...'.format(i)
        click(1025, 580, 3, hint='use')
        click(1025, 580, 1, hint='any')



