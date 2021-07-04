#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

ntimes = int(os.environ.get('ntimes', 20))

if __name__ == '__main__':
    hit_count = 0
    for i in range(ntimes):
        click(530, 450, 1, hint='enhance')
        # 3plug is about 0.92+
        if click_on('4plus', do_click=False, maxVal=0.97):
            click(730, 450, 0, hint='save')
            hit_count += 1
        else:
            click(530, 450, 0, hint='no save')
        print '#{}, hit {}, {:.3}%'.format(i, hit_count, (float(hit_count)*100/(i+1)))

    go_home()