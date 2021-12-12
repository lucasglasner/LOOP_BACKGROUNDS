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

print("Beggining request_GOES16.py ...")
# %%
# Path to NOAA GOES16 Images Repository
NOAA_GOES16 = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/"


# Image resolution in pixels.
# Aviable options: 339x339, 678x678, 1808x1808, 5424x5424, 10848x10848
res = "1808x1808"
print("Image resolution is: "+res+" pixels.")
###############################################################################
# %%
# Make HTTP request to NOAA repository
req = ''
while req == '':
    try:
        req = requests.get(NOAA_GOES16)
        break
    except:
        print("Conection refused by the server...")
        print("Sleeping 10 seconds and trying again...")
        sleep(10)
        continue
print("Successfuly connecting to server...")
# Save repository tree in a temporary file
with open(".GOES16_DIRECTORY.txt", "w") as file:
    file.write(req.text)
    file.close()

# Use regular expression bash commands to grab latest image url
order = r'LANG=en_us_88591;cat .GOES16_DIRECTORY.txt | \
	    grep '+res+r' | \
	    grep $(date -u +%d-%b-%Y | sed -e "s/\b\(.\)/\u\1/g") | \
	    tail -n 1'
url = os.popen(order).read()
url = url.split(">")[1]
url = url.split("<")[0]
url = NOAA_GOES16 + url

# %%
# Clean directory
os.system("rm -rf .GOES16_DIRECTORY.txt")


img_code = url.split("/")[-1].split("_")[0]
# Path to downloaded image:
# outpath     = "./images"
outpath = sys.argv[1]
outpath = outpath+"/GOES16_GEOCOLOR_"+img_code+".jpg"

# Download image in desired path if doesnt already exists.
print("Latest image code: "+img_code)
if not os.path.isfile(outpath):
    os.system("wget -O "+outpath+" "+url)
    print("Done with download.")
else:
    print("Latest image already exist.")
