# -*- coding: utf-8 -*-
import time, sys
import cv2
import os
import numpy as np
import subprocess

os.chdir(os.path.dirname(__file__))

username = None
if not username:
    username = 'eddiedada'
# in pycharm shell, len(sys.argv) is 3
if len(sys.argv) == 2:
    username = sys.argv[1]

if username == 'eddiedada':
    adbname = 'emulator-5554'
else:
    adbname = 'emulator-5564'

screencap_fn='s-{}.png'.format(username)
crops_base='crops'


adb_cmd = ['adb', '-s', adbname, 'shell']
if os.name =='nt':
    adb_cmd[0]+='.exe'
# cmd_screencap = adb_cmd + ['screencap', '-p']
cmd_screencap = adb_cmd + ['screencap', '-p', '/sdcard/screen.png']
cmd_pull_scap = ['adb', '-s', adbname, 'pull', '/sdcard/screen.png', screencap_fn]
cmd_tap = adb_cmd + ['input', 'tap']
cmd_swipe = adb_cmd + ['input', 'swipe']
cmd_text = adb_cmd + ['input', 'text']
cmd_key = adb_cmd + ['input', 'keyevent']

def log(msg):
    sys.stdout.write(msg+'\n')
    sys.stdout.flush()

def startapp(appname, sleep_time=0):
    log('entering %s' % appname)
    #p=subprocess.Popen(adb_cmd+['input', 'keyevent', '26'])
    #p.communicate()
    #click(10,10)
    p=subprocess.Popen(adb_cmd+['am', 'force-stop', appname])
    p.communicate()
    p=subprocess.Popen(adb_cmd+['monkey', '-p', appname, '-c', 'android.intent.category.LAUNCHER', '1'])
    p.communicate()
    if sleep_time:
        time.sleep(sleep_time)
    log( 'waited %ds' % sleep_time)

# def screencap(rotate=True):
#     proc = subprocess.Popen(cmd_screencap, stdout=subprocess.PIPE)
#     data = subprocess.check_output(['dos2unix'], stdin=proc.stdout)
#     proc.wait()
#
#     with open(screencap_fn, 'w') as f:
#         f.write(data)
#         f.close()
#     # if rotate:
#     #     subprocess.Popen(['convert', '-rotate', '-90', screencap_fn, screencap_fn]).wait()

def screencap():
    subprocess.check_output(cmd_screencap)
    subprocess.check_output(cmd_pull_scap)


def match_image(crop, capture, val):
    image = cv2.imread(capture)
    template = cv2.imread(crop)

    result = cv2.matchTemplate(image,template,cv2.TM_CCORR_NORMED)
    minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(result)
    log( 'matching %s, maxVal=%f, val=%f' % (crop, maxVal, val))
    #loc = np.where(result>0.99)

    if maxVal>=val:
        return maxLoc[0], maxLoc[1]
    else:
        return -1, -1


def click(x, y, sleep_time=0, hint=''):
    p=subprocess.Popen(cmd_tap+[str(x+5),str(y+5)])
    p.communicate()
    log('click on (%d, %d) wait %ds -- %s' % (x, y, sleep_time, hint))
    if sleep_time:
        time.sleep(sleep_time)

def swipe(x1, y1, x2, y2, sleep_time=0):
    log('swipe (%d, %d) -> (%d, %d)' % (x1, y1, x2, y2))
    p=subprocess.Popen(cmd_swipe+[str(x1), str(y1), str(x2), str(y2), '2000'])
    p.communicate()

    if sleep_time:
        time.sleep(sleep_time)


def crop_filename(image):
    return os.path.join(crops_base, image)+'.png'


def click_on(image, sleep_time=0, update_screen=True, maxVal=0.9999, shift_x=0, shift_y=0, do_click=True, retry=1):
    for _ in range(0, retry):
        if update_screen:
            screencap()
        x, y = match_image(crop_filename(image), screencap_fn, maxVal)
        log( 'match %s => (%d,%d)'%(image,x,y))
        if x != -1:
            if do_click: click(x+shift_x, y+shift_y, sleep_time)
            return True

    return False


def input_text(text, sleep_time=0):
    p = subprocess.Popen(cmd_text + [text])
    p.communicate()
    if sleep_time:
        time.sleep(sleep_time)


def go_home():
    p = subprocess.Popen(cmd_key + ['3'])
    p.communicate()

