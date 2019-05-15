#!/bin/bash
:
# Place this script in  /usr/local/bin/ as startx11vnc.sh
# create a vncpasswd 
#x11vnc -passwdfile /root/.vnc/passwd


#AUTH=`x11vnc -findauth`
#x11vnc -auth guess


x11vnc -xkb -noxrecord -noxfixes -noxdamage -display :0 -auth /var/run/lightdm/root/:0 -passwdfile /root/.vnc/passwd
