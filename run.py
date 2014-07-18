# -*- coding: utf-8 -*-
'''
Created on 03-02-2013

@author: bzyx
'''

from rincewind import RincewindFactory as factory
import sys
from twisted.internet import reactor
from twisted.python import log

if __name__ == '__main__':
    # initialize logging
    log.startLogging(sys.stdout)

    print sys.argv[1], " ",  sys.argv[2]
    # create factory protocol and application
    f = factory.RincewindFactory(sys.argv[1], sys.argv[2])

    # connect factory to this host and port
    #reactor.connectTCP("irc.freenode.net", 6667, f)
    reactor.connectTCP("IRC.Quakenet.org", 6667, f)

    # run bot
    reactor.run()
