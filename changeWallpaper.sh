image = head -n 1 dir.txt 

defaults write com.apple.desktop Background “{default = {ImageFilePath=’$image’; };}”; killall Dock