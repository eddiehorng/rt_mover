#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

exams=((830, 400), (350, 400))
exam_levels=(('exam1', 548, 490), ('exam2', 786, 490), ('exam3', 1022, 490))

if __name__ == '__main__':
    game_name='exam_entry'

    for ex, ey in exams:
        startapp_and_go_compmode(920,300, game_name, 0, debug_no_start_app=False)
        click(ex, ey, 3, hint='enter test')
        for r in range(0, 80):
            # always click 1st
            click(exam_levels[0][1], exam_levels[0][2], 2, hint='diffcult')
            if (r+1) % 3 == 0:
                click(640, 490, 1, hint='3%')
                click(1048, 670, 1, hint='confirm')
            if (r+1) % 5 == 0:
                click(1048, 670, 1, hint='confirm')







