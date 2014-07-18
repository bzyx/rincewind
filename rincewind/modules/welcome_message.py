'''
Created on 04-02-2013

@author: bzyx
'''
from __future__ import unicode_literals
import random
from rincewind.db import db
from rincewind.db.models import WelcomeMsgModel
import time


class WelcomeMsg(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        random.seed(time.time())

    def addWelcomeMesage(self, text):
        f = WelcomeMsgModel(text)
        db.save(f)
        db.commit()

    def getRandomWelcomeMsg(self):
        all=db.load(WelcomeMsgModel)
        print all
        randomMsg = random.choice(all)
        return randomMsg.text.encode('utf-8')
