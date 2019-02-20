#!/usr/bin/env python

import pika
from cryptography.fernet import Fernet

MSG = "HERP DERP PLZ IGNORE DERPY DERP"
MSGBYTES = str.encode(MSG)

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(MSGBYTES)
token
DEC = f.decrypt(token)

#print(DEC)

RESULT = DEC.decode("utf-8")
print(RESULT)
