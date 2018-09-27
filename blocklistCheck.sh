#!/bin/bash
:
#Written by Goose Sept 27 2018
REV=`echo $1 | awk -F. '{print $4"."$3"." $2"."$1}'`
RESULT=`host -t any $REV.bl.blocklist.de`

#echo $RESULT

if [[ $RESULT = *"NXDOMAIN"* ]];
        then
                echo "Not found"

        else
                echo $RESULT
                #echo $RESULT >> /opt/log/blockcheck.log
        fi
