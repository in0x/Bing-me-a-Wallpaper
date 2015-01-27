# Bing me a Wallpaper

This is a small tool written in Python that downloads the daily wallpaper from bing.com, stores it in an archive 
and changes it to your wallpaper

The way I have it set up currently is, that I have a cronjob to execute the bing.py script automatically daily. I then set my Desktop-background-rotation to the folder bing.py made and store the pictures in.

If you dont know how to set cronjobs you can use setCronJob.sh, which explain the syntax and then opens the appropriate file for you.

If any of the files are not working you can try to set execute permission by executing "chmod #x FILEPATH" (gives execute right for the file)

Currently works on OSX, but I'd like to add other OSes soon.
