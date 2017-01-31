#!/bin/sh
:
# MOTD script, place in /etc/profile.d/

honkfortune.py
echo " "
echo ""
Server Summary


echo ""
uptime

echo ""
free -m
echo ""
echo "Disk space:"
df -h / | grep / | awk ' {print $2 , $3 , $4, $5 , $6}'
df -h /apps | grep apps | awk ' {print $2 , $3 , $4, $5 , $6}'
echo " "
echo "Users Logged in:"
who  | awk ' {print $1}' | sort -u
echo " "
