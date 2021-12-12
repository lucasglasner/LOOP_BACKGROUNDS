#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 22:43:44 2021

@author: lucas

# =============================================================================
# Script for removing NOAA logo from a GOES16 Image in jpg format. 
# =============================================================================

"""

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

print("Beggining removelogo_GOES16.py ...")
# %%
path = sys.argv[1]
# Read GOES16 image
img = plt.imread(path).copy()
img.setflags(write=1)
# Image resolution in pixels.
# Aviable options: 339x339, 678x678, 1808x1808, 5424x5424, 10848x10848
res = str(img.shape[0])+"x"+str(img.shape[1])
print("Image resolution is: "+res+" pixels.")
if res in ["339x339", "678x678", "1808x1808", "5424x5424", "10848x10848"]:
    pass
else:
    raise Exception("Sorry, "+res+" is not a valid pixel image resolution.")
    os.system("exit")

if res == "1808x1808":
    print("Editing image...")
    # Move date and hour to upper left corner
    img[50:28+50, :245, :] = img[-img.shape[0]//65:, 500:745, :]
    # Invert black to white and viceversa
    img[50:28+50, :245, :] = np.where(img[50:28+50, :245, :] > 100, 0, 255)
    # Remove bottom white line
    img[-(img.shape[0]//55):, :, :] = 1
    # Remove NOAA logo
    img[-220:, :180, :] = 1

    # Overwrite image
    plt.imsave(path, img)
    print("Done")
else:
    raise Exception("Sorry, 1808x1808 is the only valid resolution for now")
    os.system("exit")
