#!/usr/bin/env python2.7

import os
import sys

with os.popen('netstat -an | grep tcp | grep EST | wc -l') as f:
    data=f.readline()

num1=int(sys.argv[1])
num2=int(sys.argv[2])
data=int(data)

if data < num1:
    print 'OK -connect counts is %d'%data
    sys.exit(0)
if data >num1 and data < num2:
    print 'Warning -connect counts is %d'%data
    sys.exit(1)

if data >num2:
    print 'Critical -connect counts is %d'%data
    sys.exit(2)

