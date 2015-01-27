chmod +x 
echo "Enter how often you'd like to check for new wallpapers"
echo
echo "for example, for everyday at 11 write * 11 * * *"
echo
echo "for every 50 minutes you could write 50 * * * *"
echo
echo "then enter the path where bing.sh is stored (you can drag and drop into terminal)"
echo
echo "press control + o to accept your entry and control + x to exit"
echo
echo "press any key to continue"
read -n 1 -s
env EDITOR=nano crontab -e

echo "if everything worked you should see crontab: installing new crontab"
echo "if not, you can manually write the cronjob by entering env EDITOR=nano crontab -e"
