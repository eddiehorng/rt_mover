#!/usr/bin/python
import datetime
from utils import *

start_loc=[[177,415],[525,529],[180,787],[512,970]]

appname='com.senjiahk.fleet'


if __name__ == '__main__':
    startapp(appname, 50)
    click(630, 680, 2)
    click_on('enter_game', 15)
    click_on('ccenter', 1)
    click_on('enter', 1)
    swipe(1000, 250, 300, 300)
    swipe(1000, 250, 300, 300)
    click_on('champ_game', 1)

    today8=datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())+datetime.timedelta(hours=20)
    today830=today8+datetime.timedelta(minutes=30)
    while True:
        now=datetime.datetime.now()
        if not (now>today8 and now<today830):
            break
        click(640, 390, 2)  #match
        click(640, 660, 2)  #fight
    print 'Bye, its %s' % datetime.datetime.now()


