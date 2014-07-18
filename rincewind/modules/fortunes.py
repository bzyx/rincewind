# -*- coding: utf-8 -*-
'''
Created on 03-02-2013

@author: bzyx
'''
#import minidb
from __future__ import unicode_literals
import random
from rincewind.db.models import FortuneModel
from rincewind.db import db
import time


class Fortunes(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        random.seed(time.time())

    def addFrotune(self, textOfFortune):
        f = FortuneModel(textOfFortune)
        db.save(f)
        db.commit()

    def getRandomForutne(self):
        allFortunes = db.load(FortuneModel)
        print "ALL fortunes", allFortunes
        for f in allFortunes:
            print "fortune ", f.text
        randomFortune = random.choice(allFortunes)
        return randomFortune.text.encode('utf-8')
