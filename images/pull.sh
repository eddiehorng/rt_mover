adb shell ls /sdcard/Pictures/Screenshots|dos2unix|grep 2016-07|awk '{print "adb pull /sdcard/Pictures/Screenshots/"$1" ."}'|sh
