import urllib
import urllib2
import os
import getpass
import subprocess
import sys

#get the current login name
userName = getpass.getuser()

bingSave = False;
#check if the user already has a wallpaper dir, if yes make a "bing" one
#if not make one
if os.path.exists("/Users/" + userName + "/Pictures/Bingwallpapers") :
	bingSave = True;
elif os.path.exists("/Users/" + userName + "/Pictures/wallpapers") :
	os.makedirs("/Users/" + userName + "/Pictures/BingWallpapers")
	bingSave = True
elif not os.path.exists("/Users/" + userName + "/Pictures/wallpapers") :
	os.makedirs("/Users/" + userName + "/Pictures/wallpapers")
	bingSave = False

#Get the html code from bing
httpString = urllib2.urlopen("http://www.bing.com/#").read()

url = ""

#build the relative url of the image, assuming they dont 
#change the directory on me (cheeky bing people)
for x in range(1, 56) :
	url += httpString[45489 + x]

#change the desired resolution of the image
url = url.replace("1366x768", "1920x1200")

#build a total url to download the file
totalURL = "http://www.bing.com/az/" + url

#extract the image name for saving
imageName = url[12:]

#change to image directory for saving
if not (bingSave) :
	directory = ("/Users/" + userName + "/Pictures/wallpapers")
	os.chdir(directory)
elif (bingSave) :
	directory = ("/Users/" + userName + "/Pictures/BingWallpapers")
	os.chdir(directory)

#create a connection instance and download the image + save it
imageInstance = urllib.URLopener()
imageInstance.retrieve(totalURL, imageName) 
urllib.urlcleanup()

os.chdir(sys.path[0])
imagePos = directory + imageName
text_file = open("dir.txt", 'w')
text_file.close()
text_file = open("dir.txt", 'r+')
text_file.write(imagePos + "\n")
text_file.write(sys.path[0])
