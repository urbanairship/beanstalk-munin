#!/usr/bin/env python
"""Reports age of waiting jobs in tubes."""
import os
import sys
import beanstalkc

HOST = os.environ.get('HOST', 'localhost')
PORT = os.environ.get('PORT', 11300)
TUBES = os.environ.get('TUBES', 'default').split()

def clean_tube(tube):
    return tube.replace('.', '_')

def do_data():
    bs = beanstalkc.Connection(HOST, PORT)
    for tube in TUBES:
        bs.use(tube)
        j = bs.peek_ready()
        val = j.stats()['age'] if j else 0
        print '%s_jobs.value %d' % (clean_tube(tube), val)

def do_config():
    print "graph_title Job Age"
    print "graph_vlabel Max Age"
    print "graph_category Beanstalk"
    print "graph_args --lower-limit 0"
    print "graph_scale no"
    for tube in TUBES:
        ctube = clean_tube(tube)
        print "%s_jobs.label %s" % (ctube, ctube)
        print "%s_jobs.type GAUGE" % ctube
        print "%s_jobs.min 0" % ctube


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'config':
        do_config()
    else:
        do_data()
