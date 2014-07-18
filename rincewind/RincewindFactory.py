# -*- coding: utf-8 -*-
'''
Created on 03-02-2013

@author: bzyx
'''

from twisted.internet import reactor
from twisted.internet import protocol
from rincewind.RincewindTheBot import RincewindTheBot

class RincewindFactory(protocol.ClientFactory):
    """A factory for LogBots.

    A new protocol instance will be created each time we connect to the server.
    """

    def __init__(self, channel, filename):
        self.channel = channel
        self.filename = filename

    def buildProtocol(self, addr):
        p = RincewindTheBot()
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed:", reason
        reactor.stop()
