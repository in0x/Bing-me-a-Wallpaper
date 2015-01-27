python bing.py
img=$(head -n 1 dir.txt)
#echo "$img"
osascript -e "tell application \"System Events\" to set picture of every desktop to \"$img\""

