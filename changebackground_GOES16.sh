#bin/bash

#Created on Sat Nov 20 14:51:06 2021
#@author: lucas
# =================================================================================================
# Script for changing gnome desktop background to the latest full disk GOES16 
# image. 
# =================================================================================================




# Get the Real Username
RUID=$(who | awk 'FNR == 1 {print $1}')

# Translate Real Username to Real User ID
RUSER_UID=$(id -u ${RUID})

#Directory where to store downloaded images
imgdir=/home/lucas/programs/LOOP_BACKGROUND/images

#if [ $(nmcli radio wifi) == enabled ]; then
    #If exist internet connection...
echo Downloading...
sudo -u ${RUID} DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/${RUSER_UID}/bus" $imgdir/.././request_GOES16.py $imgdir  #Download latest image
#Set latest downloaded image to desktop background
filename=$(ls -t $imgdir/GOES16_GEOCOLOR_* | head -n 1)
filename=${filename#$imgdir}
echo Done with download.
echo Setting "'file://${imgdir}/${filename}'" as desktop background
#gsettings set org.gnome.desktop.background picture-options "scaled"
#gsettings set org.gnome.desktop.background picture-uri file://$imgdir/$filename
sudo -u ${RUID} DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/${RUSER_UID}/bus" dconf write "/org/gnome/desktop/background/primary-color" "'#000000'"
sudo -u ${RUID} DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/${RUSER_UID}/bus" dconf write "/org/gnome/desktop/background/picture-options" "'scaled'"
sudo -u ${RUID} DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/${RUSER_UID}/bus" dconf write "/org/gnome/desktop/background/picture-uri" "'file://$imgdir/$filename'"
#Remove images
if [ $(ls $imgdir | grep GOES16_GEOCOLOR -c) -gt 6 ]; then
    list=$(ls -t $imgdir/GOES16_GEOCOLOR_* | tail -n5)
    rm -rf $list
fi
