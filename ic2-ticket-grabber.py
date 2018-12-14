#!/usr/bin/env python

# -*- coding: utf-8 -*-

#Written by goose 12/13/2018

import requests
import sys
import simplejson as json

USER = 'apiuser'
PASSWORD = 'apassword'
TGT = sys.argv[1]
URL = 'https://icinga2master.domain.com:5665/v1/actions/generate-ticket'

session = requests.session()

headers = {
    'Accept': 'application/json',
    }

payload = '{ "cn": "' + TGT + '", "pretty": true }'

RT = session.post(URL, auth=(USER, PASSWORD), data=payload, headers=headers, verify=False)
results = json.loads(RT.content)

for k, v in results.items():
    print( v[0]['ticket'])
