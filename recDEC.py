#!/usr/bin/env python

import pika
from cryptography.fernet import Fernet

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

salt = 'IvU3clMMMeFgfH35tPZWYuvvRstd3Ul9uiwQGKcsYbs='
key = str.encode(salt)
f = Fernet(key)
#
#DEC = f.decrypt(token)

def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    print(" [x] Received %r" )
    DEC = f.decrypt(body)
    RESULT = DEC.decode("utf-8")
    print(RESULT)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
