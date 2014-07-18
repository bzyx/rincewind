'''
Created on 03-02-2013

@author: bzyx
'''


class Answer(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.who = "" #if who is None else who
        self.message = "" #if initMessage is None else initMessage
        self.channel = ""

    def make_privateMSG(self, who):
        self.channel = who
        self.who = ""

    def make_toMSG(self, channel, who):
        self.channel = channel
        self.who = who

    def make_MSG(self, channel):
        self.channel = channel
        self.who = ""

    def set_text(self, text):
        self.message = text

    def append_text(self, text):
        self.message += str(text)

    def get_channel(self):
        return self.channel

    def get_message(self):
        if (len(self.who) == 0):
            return self.message
        else:
            return "%s : %s" % (self.who, self.message)

    def clear_MSG(self):
        self.who = ""
        self.channel = ""
        self.message = ""

    def appendMessage(self, message):
        self.message += str(len(message))
        
    def getWho(self):
        return self.who
    
    def getMessage(self):
        return self.message