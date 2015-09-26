#!/usr/bin/env python2.7


import os
import sys

str1='usr/lib/jvm/java-1.7.0/bin/java -Xmx1024m -cp /opt/app/logcollector/flume/conf:/opt/app/logcollector/flume/lib/*:/opt/app/logcollector/flume/plugins.d/kafka-sink/lib/*:/opt/app/logcollector/flume/plugins.d/kafka-sink/libext/* -Djava.library.path= org.apache.flume.node.Application'
with os.popen('ps -ef | grep flume ') as f:
    dt=f.readlines()
    data=''.join(dt)
if str1 in data:
    print 'Process flume is on working now !'
    sys.exit(0)

else:
    print 'Critical Process flume is stoped !!!'
    sys.exit(2)
