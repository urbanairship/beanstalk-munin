#!/usr/bin/env python
import os
import sys
import beanstalkc

HOST = os.environ.get('HOST', 'localhost')
PORT = os.environ.get('PORT', 11300)

def do_data():
    stats = beanstalkc.Connection(HOST, PORT).stats()
    print 'connections.value %d' % stats['current-connections']

def do_config():
    print "graph_title Open connections"
    print "graph_vlabel Connections"
    print "graph_category Beanstalk"
    print "graph_args --lower-limit 0"
    print "graph_scale no"
    print "connections.label Connections"
    print "connections.min 0"


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'config':
        do_config()
    else:
        do_data()
