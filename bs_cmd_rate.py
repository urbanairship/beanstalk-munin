#!/usr/bin/env python
import os
import sys
import beanstalkc

HOST = os.environ.get('HOST', 'localhost')
PORT = os.environ.get('PORT', 11300)

cmds = [ ['put', 'cmd-put', 'Put'],
         ['reserve', 'cmd-reserve', 'Reserve'],
         ['reserve_timeout', 'cmd-reserve-with-timeout', 'Reserve with timeout'],
         ['delete', 'cmd-delete', 'Delete'],
         ['touch', 'cmd-touch', 'Touch'],
         ['release', 'cmd-release', 'Release'],
         ['bury', 'cmd-bury', 'Bury'] ]

def do_data():
    stats = beanstalkc.Connection(HOST, PORT).stats()
    for j in cmds:
        print 'cmd_%s.value %d' % (j[0], stats[j[1]])

def do_config():
    print "graph_title Command Rate"
    print "graph_vlabel Commands per ${graph_period}"
    print "graph_category Beanstalk"
    print "graph_args --lower-limit 0"
    print "graph_scale no"
    for j in cmds:
        print 'cmd_%s.label %s' % (j[0], j[2])
        print 'cmd_%s.type DERIVED' % j[0]
        print 'cmd_%s.min 0' % j[0]

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'config':
        do_config()
    else:
        do_data()
