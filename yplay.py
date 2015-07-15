#!/usr/bin/python

import cv2
import numpy as np
import subprocess

'''
image = cv2.imread("testimage.bmp")
template = image[30:40,30:40,:]

result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
print np.unravel_index(result.argmax(),result.shape)
'''

adb_cmd = ['adb', 'shell']
cmd_screencap = adb_cmd + ['screencap', '-p']
cmd_tap = adb_cmd + ['input', 'tap']

screencap_fn='s.png'

endless_crops=['endless_crop2.png',  'attack_crop.png', 'gameover_crop.png', 'gift_crop.png', 'continue_crop.png', 'dialog_crop.png' , 'iknow_crop.png', 'playing_crop.png' , 'attack1_crop.png']

def screencap():
    proc = subprocess.Popen(cmd_screencap, stdout=subprocess.PIPE)
    data = subprocess.check_output(['dos2unix'], stdin=proc.stdout)
    proc.wait()
    with open(screencap_fn, 'w') as f:
        f.write(data)
        f.close()


def match_image(template, capture):
    image = cv2.imread(capture)
    template = cv2.imread(template)

    result = cv2.matchTemplate(image,template,cv2.TM_CCORR_NORMED)
    minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(result)
    #loc = np.where(result>0.99)

    if maxVal==1.0:
        return maxLoc[0], maxLoc[1]
    else:
        return -1, -1

if __name__ == '__main__':
    for crop in endless_crops:
        screencap()

        x, y = match_image(crop, screencap_fn)
        print '%s => (%d,%d)'%(crop,x,y)
        if x != -1:
            subprocess.Popen(cmd_tap+[str(x+5),str(y+5)])
            break