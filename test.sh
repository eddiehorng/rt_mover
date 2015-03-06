#!/bin/bash
function test()
{
    declare -a sc=("${!1}")
    declare -a ha=("${!2}")
    
    echo ${sc[@]}
    echo $ha
    if [ ! $ha ]; then
        echo ha
    fi
}

sc_gameover=( '200x55+132+682' 'g_crop.png' )
do=( 1 )
test sc_gameover[@] do[@]