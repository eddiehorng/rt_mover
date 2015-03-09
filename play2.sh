#!/bin/bash

adb_cmd='sudo adb shell'
tap='input tap'
logfile='log.txt'

check_match_period=6

# ctrl_endless=( '160x60+56+1130' 'endless_crop.png' 175 1160)
# ctrl_attack=( '192x32+268+1120' 'attack_crop.png' 360 1140)
# ctrl_gameover=( '200x55+132+682' 'gameover_crop.png' 235 715)
# ctrl_gift=( '186x48+264+888' 'gift_crop.png' 355 905)
# ctrl_continue=( '200x48+98+1120' 'continue_crop.png' 355 905)
# ctrl_network=( '580x110+80+685' 'dialog_crop.png' 510 735)

declare -a c0=( '160x60+56+1130' 'endless_crop.png' 175 1160 0)
declare -a c1=( '192x32+268+1120' 'attack_crop.png' 360 1140 0)
declare -a c2=( '200x55+132+682' 'gameover_crop.png' 235 715 0)
declare -a c3=( '186x48+264+888' 'gift_crop.png' 355 905 0)
declare -a c4=( '200x48+98+1120' 'continue_crop.png' 195 1150 0)
declare -a c5=( '580x110+80+685' 'dialog_crop.png' 510 735 0)
c_num=6

function printlog()
{
    msg=$1
    prefix_time=`date "+%Y/%m/%d %H:%M:%S"`
    echo $prefix_time" "$msg 
}

function appeared()
{
    location=$1
    pic=$2
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

while true
do
    $adb_cmd screencap -p | sed 's/\r$//' > screen.png
    for (( i=0;i<$c_num;i++ ))
    do
        var="c"$i"[0]"
        location=${!var}
        var="c"$i"[1]"
        pic=${!var}
        var="c"$i"[2]"
        x=${!var}
        var="c"$i"[3]"
        y=${!var}
        last_occur_var="c"$i"[4]"        
        last_occur=${!last_occur_var}
        
        # echo ${!var}
#         echo $location
#         echo $pic
        convert screen.png -crop $location tmp.png
        s=`compare -metric MAE tmp.png $pic null: 2>&1`
        if [ "$s" = "0 (0)" ]; then             
            start=$last_occur
            now=$(date +%s)
            diff=`echo $((now-start)) | awk '{print int($1/60)":"int($1%60)}'`
            printlog "Found $pic -- $diff"
            let $last_occur_var=$now
            $adb_cmd $tap $x $y
            break
        fi
    done
    sleep $check_match_period
done