#!/bin/bash

adb_cmd='sudo adb shell'
tap='input tap'
swipe='input swipe'
logfile='log'

check_match_period=3


declare -a c0=( '270x80+26+1130' 'endless_crop2.png' 175 1160 0)
declare -a c1=( '192x32+268+1120' 'attack_crop.png' 360 1140 0)
declare -a c2=( '200x55+132+682' 'gameover_crop.png' 235 715 0)
declare -a c3=( '186x48+264+888' 'gift_crop.png' 355 905 0)
declare -a c4=( '200x48+98+1120' 'continue_crop.png' 195 1150 0)
declare -a c5=( '580x110+80+685' 'dialog_crop.png' 510 735 0)
declare -a c6=( '192x42+264+970' 'iknow_crop.png' 264 970 0)
#declare -a c7=( '37x27+342+964' 'fly_crop.png' 342+387 964+1010 0)
declare -a c7=( '78x1+166+18' 'playing_crop.png' 342+387 964+946 0)
declare -a c8=( '100x32+188+1120' 'attack1_crop.png' 190 1122 0)
c_num=9

once_moved=0
swipe_delay=24

function printlog()
{
    msg1=$1
    msg2=$2
    prefix_time=`date "+%Y/%m/%d %H:%M:%S"`
    today=`date "+%Y/%m/%d"`
    times=`cat $logfile | grep "$today" | grep "$msg1" -c`
    log=$prefix_time" "$msg1" -- "$msg2" #"$times
    echo $log
    echo $log >> $logfile
}


while true
do
    $adb_cmd screencap -p 2>/dev/null | sed 's/\r$//' > screen.png 
    if [ -s screen.png ]; then
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
                if [ $last_occur -eq 0 ]; then
                    diff='1st hit'
                else
                    diff=`echo $((now-start)) | awk '{print int($1/60)":"int($1%60)}'`
                fi
                let $last_occur_var=$now
                if [[ $x == *"+"* ]] || [[ $x == *"-"* ]]; then
		    if [ $once_moved -eq 0 ]; then
			sleep $swipe_delay
			once_moved=1
                  xx=( `echo $x | sed 's/[\+|\-]/ /'` )
                  yy=( `echo $y | sed 's/[\+|\-]/ /'` )
                  printlog "Swipe ${xx[0]} ${yy[0]} ${xx[1]} ${yy[1]}"
                  $adb_cmd $swipe ${xx[0]} ${yy[0]} ${xx[1]} ${yy[1]}
		    fi
                else
		  printlog "Found $pic" $diff
                  $adb_cmd $tap $x $y
                fi
		if [ $pic = "gameover_crop.png" ]; then
		  once_moved=0
		fi
                break
            fi
        done
    fi
    sleep $check_match_period
done
