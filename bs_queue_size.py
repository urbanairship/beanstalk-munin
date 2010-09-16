#!/usr/bin/env python
import os
import sys
import beanstalkc

HOST = os.environ.get('BEANSTALK_HOST', 'localhost')
PORT = os.environ.get('BEANSTALK_PORT', 11300)

def do_data():
    stats = beanstalkc.Connection(HOST, PORT).stats()
    print 'queue_size.value %d' % stats['current-jobs-ready']

def do_config():
    print "graph_title Queue Size"
    print "graph_vlabel # of jobs in the queue"
    print "graph_args --lower-limit 0"
    print "graph_scale no"
    print "queue_size.label Jobs"
    print "queue_size.type DERIVE"
    print "queue_size.min 0"

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'config':
        do_config()
    else:
        do_data()
