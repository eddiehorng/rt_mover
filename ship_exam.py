#!/usr/bin/python
import datetime
from utils import *
from ship_common import *

exams=('exam_right', 'exam_left')
#exams=('exam_left', 'exam_right')
exam_levels=(('exam1', 548, 490), ('exam2', 786, 490), ('exam3', 1022, 490))

def handle_got_box():
    #click(1040, 490)    # sliver box
    click(640, 490)    # attack box
    if not (click_on('confirm') or click_on('get_gift')):
        return False
    else:
        return True

if __name__ == '__main__':
    game_name='exam_entry'

    has_gift=0
    for ex in exams:
        if not startapp_and_go_compmode(game_name, 0, debug_no_start_app=False):
            log('Failed to enter %s' % game_name)
            sys.exit(0)

        time.sleep(3)

        if not click_on(ex, 3):
            log('failed to enter %s'%ex)
            continue
        for r in range(0, 85):
            log('take exam on %s, round %02d'%(ex, r))
            '''
            have_exam=False
            for exlv in exam_levels:
                if not click_on(exlv[0], do_click=False):
                    has_gift+=1
                    click(exlv[1], exlv[2], 2)
                    have_exam=True
                    handle_got_box()
                    break

            if not have_exam:
                #for exlv in exam_levels:
                click(exam_levels[0][1], exam_levels[0][2], 2)
                handle_got_box()
                #if handle_got_box():
                #    break
            '''
            # always click 1st
            click(exam_levels[0][1], exam_levels[0][2], 2)
            handle_got_box()
        for _ in range(0, 3): click(636, 40, 1)
        click_on('close_win', 1, maxVal=0.99)
    log('Got gift: %d'%has_gift)






