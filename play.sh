#!/bin/bash

adb_cmd='sudo adb shell'
tap='input tap'
logfile='log.txt'
check_gameover_init=90
check_gameover_period=10

sc_gameover=( '200x55+132+682' 'g_crop.png' )
sc_network=( '580x110+80+685' 'n_crop.png' )

function printlog()
{
    msg=$1
    prefix_time=`date "+%Y/%m/%d %H:%M:%S"`
    echo $prefix_time" "$msg >> $logfile
}

function appeared()
{
    declare -a sc=("${!1}")
    declare -a no_cap=("${!2}")
    if [ ! $no_cap ]; then
        $adb_cmd screencap -p | sed 's/\r$//' > screen.png
    fi
    convert screen.png -crop "${sc[0]}" tmp.png
    s=`compare -metric MAE tmp.png "${sc[1]}" null: 2>&1`
    if [ "$s" = "0 (0)" ]; then 
        return 1
    else
        return 0
    fi
}

function is_gameover()
{
    appeared sc_gameover[@]
    over=$?
    if [ $over -eq 0 ]; then
        # check if neterror dialog appear, but no screen capture again cause we just did that
        handle_neterror 1
        return $?
    fi 
    
    return $over
}

function handle_neterror()
{
    no_cap=( $1 )
    appeared sc_network[@] no_cap[@]
    if [ $? -eq 1 ]; then
        printlog "Network error dialog detected"
        $adb_cmd $tap 510 735
        sleep 10
        return 1
    fi
    return 0
}

printlog "Entering game"
#enter 
$adb_cmd $tap 175 1160
sleep 10
handle_neterror

#strike
$adb_cmd $tap 360 1140
sleep 3

#strike
$adb_cmd $tap 360 1140
sleep 3

#strike
$adb_cmd $tap 360 1140
sleep 3

#playing game
sleep $check_gameover_init
while true
do
    printlog "Check is gameover?"
    is_gameover
    if [ $? -eq 1 ]; then
        printlog "Gameover!"
        break    
    else
        printlog "Not gameover, wait for a while..."
        sleep $check_gameover_period
    fi    
done

sleep 8
handle_neterror

#return
$adb_cmd $tap 235 715
sleep 8
handle_neterror

#get gift
$adb_cmd $tap 355 905
sleep 3

#continue
$adb_cmd $tap 195 1150
sleep 10
printlog "Return to home"
