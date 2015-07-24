#!/bin/bash

app='com.garena.game.jettw'

source common.sh

$adb_cmd am force-stop $app
$adb_cmd monkey -p $app -c android.intent.category.LAUNCHER 1

# sleep 20
# $adb_cmd input keyevent KEYCODE_BACK
# sleep 2


declare -a c0=( '270x80+26+1130' 'endless_crop2.png' 175 1160 0)
declare -a c1=( '580x110+80+685' 'dialog_crop.png' 510 735 0)
declare -a c2=( '192x42+264+970' 'iknow_crop.png' 264 970 0)
declare -a c3=( '219x35+248+992' 'receive.png' 250 995  0)
declare -a c4=( '203x50+256+716' 'confirm.png' 260 720 0)
c_num=5

go=1
while [ $go -eq 1 ];
do
    $adb_cmd screencap -p 2>/dev/null | sed 's/\r$//' > screen.png 
    if [ -s screen.png ]; then
        for (( i=0;i<$c_num;i++ ))
        do
            var="c"$i"[0]"
            location=${!var}
            var="c"$i"[1]"
            pic=$crop_base"/"${!var}
            var="c"$i"[2]"
            x=${!var}
            var="c"$i"[3]"
            y=${!var}
            convert screen.png -crop $location tmp.png
            s=`compare -metric MAE tmp.png $pic null: 2>&1`
	    if [ "$s" = "0 (0)" ]; then  
	      printlog "Found $pic"
	      if [[ $pic == *"endless_crop2.png"* ]]; then
		printlog "Entered the game!"
		go=0
		break
	      fi
		  
              $adb_cmd $tap $x $y	
              break
            fi
        done
    fi
    sleep 3
done
# # 