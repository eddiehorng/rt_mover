#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

if __name__ == '__main__':
    game_name='boss_game'
    if not startapp_and_go_compmode(390, 360, game_name, 10):
        log('Failed to enter %s' % game_name)
        sys.exit(1)

    end_time=datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())+datetime.timedelta(hours=12,minutes=58)
    while True:
        now=datetime.datetime.now()
        if now>end_time:
            break
        click(615, 670, 1)  #enter fight
    print 'Bye, its %s' % now

    go_home()
