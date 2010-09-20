#!/usr/bin/env python
import os
import sys
import beanstalkc

HOST = os.environ.get('HOST', 'localhost')
PORT = os.environ.get('PORT', 11300)

jobs = [ ['ready', 'current-jobs-ready', 'Ready'],
         ['urgent', 'current-jobs-urgent', 'Urgent'],
         ['reserved', 'current-jobs-reserved', 'Reserved'],
         ['delayed', 'current-jobs-delayed', 'Delayed'],
         ['buried', 'current-jobs-buried', 'Buried'] ]

def do_data():
    stats = beanstalkc.Connection(HOST, PORT).stats()
    for j in jobs:
        print '%s.value %d' % (j[0], stats[j[1]])

def do_config():
    print "graph_title Queue Size"
    print "graph_vlabel Number of jobs in the queue"
    print "graph_category Beanstalk"
    print "graph_args --lower-limit 0"
    print "graph_scale no"
    for j in jobs:
        print '%s.label %s' % (j[0], j[2])
        print '%s.type GAUGE' % j[0]
        print '%s.min 0' % j[0]

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'config':
        do_config()
    else:
        do_data()
