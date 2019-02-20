#!/usr/bin/env python

import pika
from cryptography.fernet import Fernet

MSG = "HERP DERP PLZ IGNORE DERPY DERP"
MSGBYTES = str.encode(MSG)
salt = 'IvU3clMMMeFgfH35tPZWYuvvRstd3Ul9uiwQGKcsYbs='
key = str.encode(salt)
#key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(MSGBYTES)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=token)
print(" [x] Sent MSG " )
connection.close()
