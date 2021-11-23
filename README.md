## LOOP_BACKGROUNDS
---

Project for automatically change desktop background based on images downloaded from internet.
First project is made to work with the latest GOES16 Full Disk GEOCOLOR image. The program ./request_GOES16.py [/path/to/image] is used to download
the latest GOES16 image aviable on NOAA public website. After that the program ./changebackground_GOES16.sh is responsable of calling the python program
as set the image as the current desktop background. Finally an example of my "crontab -e" output is shared as an example of my pc, where the latest GOES 
image changes every 15 minutes. 



