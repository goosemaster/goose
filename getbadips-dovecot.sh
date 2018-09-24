#!/bin/bash
:
# Written by goose 9/24/2018

# Regular doveclients do not have udc data errors, so auth failures with those messages are most likely bots

LIST=`grep "AUTH failure" /var/log/dovecot.log | grep "udc data" |  uniq -u | awk ' {print $14}' | uniq -u | sed "s/rip=//g"`

for i in $LIST
        do echo $i ; geoiplookup $i;
         fail2ban-client set dovecot banip $i
         # or Iptables
         # iptables -A INPUT -s  $i -j DROP
        done
~
