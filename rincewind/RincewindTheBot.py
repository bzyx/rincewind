# -*- coding: utf-8 -*-
'''
Created on 03-02-2013

@author: bzyx
'''
from twisted.words.protocols import irc
import time
import random
from rincewind.utils import Answer
from rincewind.modules.people import PeopleManager
from rincewind.modules.fortunes import Fortunes
from rincewind.modules.message_logger import MessageLogger
import datetime
import calendar
from rincewind.utils.cmd_dispather import CMD
from rincewind.utils.fun_dispather import Functions
from rincewind.modules.welcome_message import WelcomeMsg


class RincewindTheBot(irc.IRCClient):
    """A logging IRC bot."""

    nickname = "Rincewind"
    realname = "HEX"
    username = "Maggus"
    fortunes = Fortunes()
    peopleMgr = PeopleManager()
    cmd_mgr = CMD()
    fun_mgr = Functions()
    welcome_controller = WelcomeMsg()
    users = []

    def connectionMade(self):
        print "[connectionMade]"
        self._names = {}
        irc.IRCClient.connectionMade(self)
        self.logger = MessageLogger(
                                    open(self.factory.filename, "a"))
        self.logger.log("[connected at %s]" %
                        time.asctime(time.localtime(time.time())))
        random.seed(time.time())

    def connectionLost(self, reason):
        print "[connectionLost] "+reason
        irc.IRCClient.connectionLost(self, reason)
        self.logger.log("[disconnected at %s]" %
                        time.asctime(time.localtime(time.time())))
        self.logger.close()

    def signedOn(self):
        print "[signedOn]"
        """Called when bot has succesfully signed on to server."""
        self.join(self.factory.channel)

    def joined(self, channel):
        print "[joined] "+ channel
        """This will get called when the bot joins the channel."""
        self.logger.log("[I have joined %s]" % channel)
        self.describe(channel, self.welcome_controller.getRandomWelcomeMsg())
#        self.describe(channel, random.choice(["Wpadamy w panikę?", "Kto py­ta – ten zbłądził.", \
#                                               "Powszechnie wiadomo, że kamień potrafi myśleć. Na tym fakcie opiera się cała elektronika.", \
#                                               "Szanse jeden na milion mają to do siebie, że sprawdzają się w dziewięciu na dziesięć przypadków.",\
#                                               "Oni nie wiedzą więcej niż zwykli ludzie, którzy nawet nie wiedzą, że tego nie wiedzą."]))

    def privmsg(self, user, channel, msg):
        print "privmsg user:" + user + " channel: " + channel + " msg :" + msg
        """This will get called when the bot receives a message."""
        user = user.split('!', 1)[0]
        self.logger.log("<%s> %s" % (user, msg))

        # Check to see if they're sending me a private message
        if channel == self.nickname:
            #msg = "It isn't nice to whisper!  Play nice with the group."
            #self.msg(user, msg)

            if (msg.strip().startswith("cmd")):
                context = {"channel": channel,
                           "user": user,
                           "currentMessage": msg}
                self.cmd_mgr.paraseCMD(msg.split("cmd")[1], context)
                #self.msg(channel, self.cmd_mgr.getAnser().getMessage())
                self.msg(self.cmd_mgr.getAnser().get_channel(),
                         self.cmd_mgr.getAnser().get_message())

            return

        # Otherwise check to see if it is a message directed at me
        if msg.startswith(self.nickname + ":"):
            # liczyć goroli
            # odliczyć boty
            # bufa, evaneca i hermetica
            #if all(w in "dycki tyś nima bot ?" for w in ('bot', '?'))s

            print msg.split(":")[1]
            print msg.split(":")[1]
            # print msg.lower().split("cmd")[1]

            context = {"channel": channel, "user": user,
                       "currentMessage": msg, "users": self.users}
            self.fun_mgr.paraseCMD(msg.split(":")[1], context)
            self.msg(self.fun_mgr.getAnser().get_channel(),
                     self.fun_mgr.getAnser().get_message())

#            else:
#                chosenMSG = random.choice(["%s: we internecie żodyn nie wiy, że żech je psym... żodyn...",\
#                                           "%s: Żodyn mnie nigdy ni słucho", \
#                                           "%s: Wylyź!",
#                                           "%s: Jo Cie prosza..."])
#                msg = chosenMSG % user
#                self.msg(channel, msg)
            self.logger.log("<%s> %s" % (self.nickname, msg))

    def action(self, user, channel, msg):
        print "action user:" + user + " channel: " + channel + " msg :" + msg
        """This will get called when the bot sees someone do an action."""
        user = user.split('!', 1)[0]
        self.logger.log("* %s %s" % (user, msg))

    # irc callbacks

    def irc_NICK(self, prefix, params):
        print "irc_NICK prefix:" + str(prefix) +" params: "+ str(params)
        """Called when an IRC user changes their nickname."""
        old_nick = prefix.split('!')[0]
        new_nick = params[0]
        self.logger.log("%s is now known as %s" % (old_nick, new_nick))

    def irc_RPL_NAMREPLY(self, prefix, params):
        print "irc_RPL_NAMREPLY prefix:" + str(prefix) +" params: "+ str(params)
        """
    Handles the raw NAMREPLY that is returned as an answer to the NAMES command
    Accumulates users until RPL_ENDOFNAMES
    """
        channel = params[2]
        users = params[3].split()
        self._names.setdefault(channel, []).extend(users)

    def irc_RPL_ENDOFNAMES(self, prefic, params):
        print "irc_RPL_ENDOFNAMES prefic:" + str(prefic) +" params: "+ str(params)
        """
    Handles the end of the RPL_NAMREPLY. This is called when all NAMREPLYs have
    finished. It calls the higher-level functions as well as fires the deferreds
    """
        channel = params[1]
        self.users = self._names.pop(channel, [])

    def names(self, channel):
        print "names channel:" + channel
        """
        Tells the server to give a list of users in the specified channel
        """
        if channel is not None:
            self._names[channel] = []
            self.sendLine("NAMES %s" % channel)

    # For fun, override the method that determines how a nickname is changed on
    # collisions. The default method appends an underscore.
    def alterCollidedNick(self, nickname):
        print "alterCollidedNick nickname:" + nickname
        """
        Generate an altered version of a nickname that caused a collision in an
        effort to create an unused related name for subsequent registration.
        """
        return nickname + '^'
