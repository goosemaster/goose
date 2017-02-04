#!/bin/bash
#Written  8 26 2011
# Script goes through files in a directory and performs sed
#pattern replacement 

if [ -z "$1" ]
        then
echo " Error input original pattern to search for "
exit 0
fi

if [ -z "$2" ]
then
        echo "Error input string to replace original pattern  "
exit 0
fi

if [ -z "$3" ]
then
        echo "Error input search string to detect correct filenames
to run fix   "
exit 0
fi

ACT=`ls $PWD | grep $3`

for i in $ACT

do
if [ -d "$i"  ]
        then
echo "File $i is a directory, skipping"
else
echo "fixing $i"
sed -e "s/$1/$2/g" $i > /tmp/test$$.out
cat /tmp/test$$.out > $i

fi

done

rm /tmp/test$$.out
