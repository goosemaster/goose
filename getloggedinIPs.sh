#!/bin/bash
:
# Written by L 9/24/2018

#Get list of ips / locations of accoutns that are currently logged in via dovecot

# grep "suc" /var/log/dovecot.log | awk ' { print $9}' | uniq -u

LIST=` grep "suc" /var/log/dovecot.log | awk ' { print $9}' | uniq -u | grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' | uniq -u `

WEBMAIL=`grep "suc" /var/log/dovecot.log | awk ' { print $9}' | uniq -u | awk '/127.0.0.1/' | wc -l`

TMPLIST='templist.txt'


echo "webmail logins:" $WEBMAIL

sleep 3

for i in $LIST
        do
          if [ $i == "127.0.0.1" ]
                then
                        #echo "ignore"
                        :

            else
                echo $i >> $TMPLIST
          fi
        done


echo "Dovecot logins:"

for i in `cat $TMPLIST`
        do
                echo $i; geoiplookup $i
        done
# Cleanup
rm $TMPLIST
