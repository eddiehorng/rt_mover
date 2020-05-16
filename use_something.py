#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

do_enter_game=False

ntimes = 500
delay=1

if __name__ == '__main__':
    for i in range(0, ntimes):
        print '#{} round ...'.format(i)
        click(1025, 580, 0, hint='use')
        if delay:
            time.sleep(3)
            click(1025, 580, 1, hint='any')



