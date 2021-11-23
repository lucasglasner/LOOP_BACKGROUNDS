#!/usr/bin/env python3
"""
Created on Sat Nov 20 14:51:06 2021

@author: lucas

# =============================================================================
# Script for downloading latest full disk GOES16 Image in jpg format. 
# =============================================================================

"""

import requests
import os
import sys
from time import sleep

#%%
#Path to NOAA GOES16 Images Repository
NOAA_GOES16 = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/"

#Request time
order       = r'date +%Y-%b-%d_%H:%M:%S | \
	      sed -e "s/\b\(.\)/\u\1/g"'
now         = os.popen(order).read()[:-1]

#Path to downloaded image:
#outpath     = "./images"   
outpath     = sys.argv[1]
outpath     = outpath+"/GOES16_GEOCOLOR_"+now+".jpg"

#Image resolution in pixels.
#Aviable options: 339x339, 678x678, 1808x1808, 5424x5424, 10848x10848
res         = "1808x1808"

###############################################################################
#%%
#Make HTTP request to NOAA repository
req = ''
while req =='':
    try:
        req = requests.get(NOAA_GOES16)
        break
    except:
        print("Conection refused by the server...")
        print("Sleeping 10 seconds and trying again...")
        sleep(10)
        continue
#Save repository tree in a temporary file
with open(".GOES16_DIRECTORY.txt","w") as file:
	file.write(req.text)
	file.close()
	
#Use regular expression bash commands to grab latest image url
order = r'cat .GOES16_DIRECTORY.txt | \
	grep '+res+r' | \
	grep $(date +%d-%b-%Y | \
	sed -e "s/\b\(.\)/\u\1/g") | \
	tail -n 1'
url = os.popen(order).read()
url = url.split(">")[1]
url = url.split("<")[0]
url = NOAA_GOES16 + url

#Clean directory
os.system("rm -rf .GOES16_DIRECTORY.txt")

#Download image in desired path
os.system("wget -O "+outpath+" "+url) 
