#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

if __name__ == '__main__':
    game_name='champ_game'
    startapp_and_go_compmode(1070, 300, game_name, 4, debug_no_start_app=0)

    today831=datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())+datetime.timedelta(hours=20, minutes=31)
    while True:
        now=datetime.datetime.now()
        if now>today831:
            break
        click(640, 390, 0.5)  #match
        click(640, 660, 0.5)  #fight
    print 'Bye, its %s' % now


