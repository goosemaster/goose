#!/bin/bash
:
# Written 01/15/2015

python -m SimpleHTTPServer 8989 &
sleep 40
pkill -P $$
kill -9 $$
