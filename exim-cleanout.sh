#!/bin/bash
:
# Exim cleanout script
# Written 9/24/2014
# Deletes messages older than 59 minutes.

exim -bpc

MLIST=`exim -bp | grep "[0-9]h" | awk '/h/ {print $3}'`
for i in $MLIST 

do

exim -Mrm $i

done

echo "Clearing frozen messages:"

exiqgrep -i -z | xargs exim -Mrm

exim -bpc
exim -bp | exiqsumm
