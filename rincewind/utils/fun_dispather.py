# -*- coding: utf-8 -*-
'''
Created on 04-02-2013

@author: bzyx
'''
from rincewind.modules.people import PeopleManager
from rincewind.utils import Answer
import datetime
import calendar
from rincewind.modules.fortunes import Fortunes
import rincewind.modules.ideagen as ideagen


class Functions(object):
    '''
    classdocs
    '''
    people_controller = PeopleManager()
    fortune_controller = Fortunes()
    answer = Answer.Answer()

    def __init__(self):
        '''
        Constructor
        '''

    def paraseCMD(self, cmd_name, context):
        cmd_stripped = cmd_name.split()
        set_striped = set(cmd_stripped)
        #[set_striped.add(s) for s in cmd_stripped]
        print type(cmd_stripped)
        #cmd_args = cmd_name.split()[1:]
        self.answer.clear_MSG()

        print cmd_stripped
        print "CONTEXT: ", context
        print set_striped
        print len(set_striped.intersection(['kto', 'je', 'gorol', 'pokoz', 'goroli']))
        print len(set_striped.intersection(['idea', 'idea!', 'idea?', 'pomysl','pomysł']))

        if "wiela" in cmd_stripped:
            #Ile ludzi na irc
            wszystkich = len(set(context['users']))
            goroli = len(set(context['users']).intersection(
                    self.people_controller.getPeopleForRole("gorol")))
            print self.people_controller.getPeopleForRole("gorol")
            botow = len(set(context['users']).intersection(
                    self.people_controller.getPeopleForRole("bot")))
            print self.people_controller.getPeopleForRole("bot")

            self.answer.make_toMSG(context['channel'], context['user'])
            self.answer.set_text("tera je " + str(wszystkich))
            self.answer.append_text(" w tym " + str(goroli) + " goroli")
            self.answer.append_text(" i " + str(botow) + " maszin")

        elif "kalyndorz" in cmd_stripped:
            #import locale
            #locale.setlocale(locale.LC_TIME, "pl_PL") # polskie nazwy sudo locale-gen pl_PL
            now = datetime.datetime.now()
            calendar.TextCalendar().prmonth(now.year, now.month)
            cal = calendar.TextCalendar().formatmonth(now.year, now.month)
            self.answer.make_toMSG(context['channel'], context['user'])
            self.answer.set_text(cal)

        elif (len(set_striped.intersection(['kto', 'je', 'gorol', 'pokoz', 'goroli'])) > 1):
            gorole = set(context['users']).intersection(
            self.people_controller.getPeopleForRole("gorol"))
            self.answer.make_toMSG(context['channel'], context['user'])
            if (len(gorole) > 0):
                self.answer.set_text("som sam " + ' '.join(gorole))
            else:
                self.answer.set_text("same hanysy")

        elif (len(set_striped.intersection(['idea', 'idea!', 'idea?', 'pomysl','pomysł'])) >= 1):
	    self.answer.make_toMSG(context['channel'], context['user'])
            self.answer.set_text(ideagen.random_idea())

        else:
            fortune_for_you = self.fortune_controller.getRandomForutne()
            self.answer.make_toMSG(context['channel'], context['user'])
            self.answer.set_text(fortune_for_you)

    def getAnser(self):
        return self.answer