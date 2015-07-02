import urllib2
import os
import getpass
import re

def main():
	#get the current login name
	userName = getpass.getuser()
	picuteRoot = "/Users/" + userName + "/Pictures/"
	savePath = picuteRoot + "BingWallpapers"

	#check if the user already has a wallpaper dir, if yes make a "bing" one
	#if not make one
	if not os.path.exists(savePath) :
		if not os.path.exists(picuteRoot + "wallpapers") :
			savePath = picuteRoot + "wallpapers"
		os.makedirs(savePath)

	#Get the html code from bing
	try:
		htmlString = urllib2.urlopen("http://www.bing.com/").read()
	except Exception, e:
		print str(e) + " - Could not read from bing.com (No connection)"
		return

	#build the relative url of the image, assuming they dont 
	#change the directory on me (cheeky bing people)
	urlRe = re.search("g_img={url:'(.*?)\.jpg'", htmlString)
	url = urlRe.group(1) + ".jpg"

	#change the desired resolution of the image
	url = url.replace("1366x768", "1920x1200")

	#build a total url to download the file
	totalURL = "http://www.bing.com" + url

	imageName = savePath + "/" + url.split('/')[-1]

	if os.path.exists(imageName):
		print "Image already exists"
		return

	print("saving image to: " + imageName)

	#create a connection instance and download the image + save it
	try:
		imageFile = urllib2.urlopen(totalURL)
		imageOut = open(imageName, 'wb')
		imageOut.write(imageFile.read())
		imageOut.close()
	except Exception, e:
		print str(e) + " - failed to load image"

	text_file = open("dir.txt", 'w')
	text_file.write(imageName + "\n")
	text_file.close()
	print("Successful")

main()
