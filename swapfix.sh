#!/bin/bash
:
# Written Aug 2014

(swapoff -a; swapon -a) & watch free -m
