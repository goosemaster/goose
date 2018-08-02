#!/usr/bin/env python

#Written by goose 7/20/2018
#
# This script is intended for use with Freeradius. It converts canopy callstation ids to mac and looks up their current 
#leased IPs within Infoblox. From there it is forwarded to radius accting as a "framed-ip"

import os
import sys
import re
import json
import requests
from requests import Request, Session
import netaddr
from netaddr import EUI

try:
        ARG = sys.argv[1]

except:
        print("")
        exit()

callstation = ARG
cs = callstation[2:]


#print(cs) #Uncomment to debug
fix  = re.sub(r'-', ":", cs)
fix2 = re.sub(r'00', '0', fix)
fix3 = fix2.lower()
remoteid = "a" + fix3
#print(remoteid) #Uncomment to debug
mac = EUI(remoteid)
mac.dialect = netaddr.mac_unix

def send_request():
    # Infoblox - Search by SM MAC

    URL = "https://infoblox.domain.tld/wapi/v2.6/lease"

    payload = {
        "_return_type": "json-pretty",
        "_return_fields": "address",
        "remote_id": mac
        }

    with requests.session() as s:
        try:
                s.auth = ('apiuser', 'secret-password')
                r = s.get(URL, data=payload)
                resp = r.json()
                print(resp[0]["address"])

        except:
                print(" ") # Silent fail to prevent bad data in radacct table


send_request()
