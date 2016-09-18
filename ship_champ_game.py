#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

if __name__ == '__main__':
    game_name='champ_game'
    if not startapp_and_go_compmode(game_name, 8):
        log('Failed to enter %s' % game_name)
        sys.exit(1)

    today831=datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())+datetime.timedelta(hours=20, minutes=31)
    while True:
        now=datetime.datetime.now()
        if now>today831:
            break
        click(640, 390, 1)  #match
        click(640, 660, 1)  #fight
    print 'Bye, its %s' % now


