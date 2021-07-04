#!/usr/bin/python
import datetime, os
from utils import *
from ship_common import *

do_enter_game=False

ntimes = int(os.environ.get('ntimes', 250))
delay = int(os.environ.get('delay', 3))

if __name__ == '__main__':
    for i in range(0, ntimes):
        print '#{} round ...'.format(i)
        click(1025, 580, 0, hint='use')
        if delay:
            time.sleep(3)
            click(1025, 580, 1, hint='any')


    go_home()
