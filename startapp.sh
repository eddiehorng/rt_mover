#!/bin/bash

app='com.garena.game.jettw'

adb_cmd='sudo adb shell'

$adb_cmd am force-stop $app
$adb_cmd monkey -p $app -c android.intent.category.LAUNCHER 1

sleep 20
$adb_cmd input keyevent KEYCODE_BACK
sleep 2
