#!/usr/bin/env python

# -*- coding: utf-8 -*-
#Written by goosemaster 3/21/2017

import requests
import sys
import simplejson as json
from pprint import pprint

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

USER = 'username'
PASSWORD = 'changeme'

AURL = 'https://apiforsaltmaster.org:8443/login'
URL = 'https://apiforsaltmaster.org:8443/'

session = requests.session()

headers = {
    'Accept': 'application/json',
    }


sdata = [('client', 'local'), ('tgt', '*'), ('fun', 'test.ping'),]

data = [
  ('username', USER),
    ('password', PASSWORD),
      ('eauth', 'pam'),
      ]

# Authenticate

r = session.post(AURL, data, verify=False)
#Access API
r2 = session.post(URL, headers=headers,  data=sdata, verify=False)

hdata = json.loads(r2.content)

print "Current salt minion status"
pprint(hdata)

