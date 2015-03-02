#!/bin/bash

adb_cmd='sudo adb shell'
tap='input tap'
logfile='log.txt'
check_gameover_init=120
check_gameover_period=10

function printlog()
{
    msg=$1
    prefix_time=`date "+%Y/%m/%d %H:%M:%S"`
    echo $prefix_time" "$msg >> $logfile
}

function is_gameover()
{
    $adb_cmd screencap -p | sed 's/\r$//' > screen.png
    convert screen.png -crop 200x55+132+682 s_crop.png
    s=`compare -metric MAE s_crop.png g_crop.png null: 2>&1`
    if [ "$s" = "0 (0)" ]; then 
        return 1
    else
        return 0
    fi
}

printlog "Entering game"
#enter 
$adb_cmd $tap 175 1160
sleep 2

#strike
$adb_cmd $tap 360 1140
sleep 2

#strike
$adb_cmd $tap 360 1140
sleep 2

#strike
$adb_cmd $tap 360 1140
sleep 2

#playing game
sleep $check_gameover_init
while true
do
    printlog "Check is gameover?"
    is_gameover
    if [ $? -eq 0 ]; then
        printlog "Not gameover, wait for a while..."
        sleep $check_gameover_period
    else
        printlog "Gameover!"
        break
    fi    
done

#return
$adb_cmd $tap 235 715
sleep 5

#get gift
$adb_cmd $tap 355 905
sleep 2

#continue
$adb_cmd $tap 195 1150
sleep 10
printlog "Return to home"