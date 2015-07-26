#!/usr/bin/python
from utils import *

def give_power(img_enter, img_power):
    if click_on(img_enter, 3):
        swipe(360, 300, 360, 700, 2)
        sent=0
        page_down=False
        while sent < 10:
            if click_on(img_power, 3, maxVal=0.99):
                click_on('next', 1)
                sent+=1
            else:
                if page_down:
                    break
                else:
                    swipe(360, 900, 360, 400, 2)
                    page_down=True

if __name__ == '__main__':
    startapp()
    give_power('endless_crop2', 'power1')
    give_power('team', 'power2')

