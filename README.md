# Bing me a Wallpaper

###Summary
This is a small tool written in Python that downloads the daily wallpaper from bing.de, stores it in an archive 
and changes it to your wallpaper.

###How to set it up and how it works
The way this works on my set-up is that i have a cronjob set for every 60th minute which executes bing.sh which:
  1. Runs bing.py, this:
      - Downloads the bing background image
      - Stores it on your machine
      - Writes the local path of the picture on your computer into dir.txt
  2. Reads the image path from dir.txt into a variable
  3. Sets that path to your desktop image via applescript

The images are also archived in your images directory. 

###Using cron
If you dont know how to set cronjobs you can use setCronJob.sh, which explain the syntax and then opens the appropriate file for you.

If any of the files are not working you can try to set execute permission by executing "chmod +x FILEPATH" (gives execute right for the file)

###Everything else
Currently works on OSX, but I'd like to add other OSes soon.

Feel free to use any of the code, I put it under the [MIT license](http://opensource.org/licenses/MIT)
