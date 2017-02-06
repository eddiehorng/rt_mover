adb shell ls /sdcard/Pictures/Screenshots|dos2unix|grep 2017-02|awk '{print "adb pull /sdcard/Pictures/Screenshots/"$1" ."}'|sh
