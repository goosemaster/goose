#!/bin/bash
:
# Written 11/12/2014

DATE=`date "+%F-%H"`

username="yourusername"
BIGFILE="bigfiles-$DATE.txt"

if [ -f $BIGFILE ]; then
   echo "File '$BIGFILE' Exists" ; rm $BIGFILE
fi

touch $BIGFILE

BIGFILES=`cat bigfiles-$DATE.txt`
USAGE=`df -h /apps | awk '/dev/ {print $5} '`
IAM=`id -u`

if [ $IAM != "0" ];
then echo "You are not root, this script must be ran as root"
exit 1
fi

# Main logic

echo "Disk usage at $USAGE "

find /apps -type f -size +100000k -exec ls -lh {} \; | awk '{ print $9 ": " $5 }'  >> bigfiles-$DATE.txt

echo "Complete file listing generated in $PWD/bigfiles-$DATE.txt"


grep ".gz" bigfiles-$DATE.txt
grep ".log" bigfiles-$DATE.txt

echo "Disk usage at $USAGE "

chown $username bigfiles-$DATE.txt
