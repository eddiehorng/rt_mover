pic=$1
x=$2
y=$3
w=$4
h=$5

convert -crop $w"x"$h"+"$x"+"$y $pic c.png
