#!/bin/sh

dladm show-phys
ipadm create-if e1000g0
ipadm create-addr -T dhcp e1000g0/v4
ipadm show-addr
