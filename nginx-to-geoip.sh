#!/bin/bash

LIST=`grep "xmlrpc.php" /var/log/nginx/website.org.log | awk ' {print $1}'`


for i in $LIST

do echo $i; geoiplookup $i

done
