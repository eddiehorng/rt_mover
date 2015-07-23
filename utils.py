import time
import cv2
import os
import numpy as np
import subprocess


adb_cmd = ['adb', 'shell']
cmd_screencap = adb_cmd + ['screencap', '-p']
cmd_tap = adb_cmd + ['input', 'tap']
cmd_swipe = adb_cmd + ['input', 'swipe']

screencap_fn='s.png'
crops_base='crops'

def startapp():
    p=subprocess.Popen(['./startapp.sh'])
    p.communicate()

def screencap():
    proc = subprocess.Popen(cmd_screencap, stdout=subprocess.PIPE)
    data = subprocess.check_output(['dos2unix'], stdin=proc.stdout)
    proc.wait()
    with open(screencap_fn, 'w') as f:
        f.write(data)
        f.close()


def match_image(crop, capture, val):
    image = cv2.imread(capture)
    template = cv2.imread(crop)

    result = cv2.matchTemplate(image,template,cv2.TM_CCORR_NORMED)
    minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(result)
    print 'matching %s, maxVal=%f, val=%f' % (crop, maxVal, val)
    #loc = np.where(result>0.99)

    if maxVal>=val:
        return maxLoc[0], maxLoc[1]
    else:
        return -1, -1


def click(x, y, sleep_time=0):
    p=subprocess.Popen(cmd_tap+[str(x+5),str(y+5)])
    p.communicate()
    if sleep_time:
        time.sleep(sleep_time)

def swipe(x, x2, y, y2, sleep_time=0):
    p=subprocess.Popen(cmd_swipe+[str(x), str(x2), str(y), str(y2)])
    p.communicate()
    if sleep_time:
        time.sleep(sleep_time)

def crop_filename(image):
    return os.path.join(crops_base, image)+'.png'

def click_on(image, sleep_time=0, update_screen=True, maxVal=0.9999):
    if update_screen:
        screencap()
    x, y = match_image(crop_filename(image), screencap_fn, maxVal)
    print 'match %s => (%d,%d)'%(image,x,y)
    if x != -1:
        click(x, y, sleep_time)
        return True
    else:
        return False
