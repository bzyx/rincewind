# -*- coding: utf-8 -*-
'''
Created on 04-02-2013

@author: bzyx
'''
from rincewind.modules.admins import Admin
from rincewind.utils import Answer
from rincewind.modules.people import PeopleManager
from rincewind.modules.fortunes import Fortunes
from rincewind.modules.welcome_message import WelcomeMsg


class CMD(object):
    '''
    classdocs
    '''

    admin_controller = Admin()
    people_controller = PeopleManager()
    fortunes_controller = Fortunes()
    welcomess_controller = WelcomeMsg()
    answer = Answer.Answer()

    def __init__(self):
        '''
        Constructor
        '''

    def paraseCMD(self, cmd_name, context):
        cmd_stripped = cmd_name.strip()
        cmd_args = cmd_name.split()[1:]
        self.answer.clear_MSG()

        print "CONTEXT: ", context

        if cmd_stripped.startswith("_adadmin_"):
            #Dodaj admina
            self.admin_controller.addAdmin(cmd_args[0], "", int(cmd_args[1]))
            self.answer.make_privateMSG(context['user'])
            self.answer.set_text("addAdmin " + cmd_args[0])

        if cmd_stripped.startswith("checkme"):
            #sprawdź upranwienia
            value = self.admin_controller.validateAdmin(cmd_args[0], "")
            self.answer.make_privateMSG(context['user'])
            self.answer.set_text("checkme " + str(value))

        if cmd_stripped.startswith("p+"):
            #Dodaj człowieka
            self.people_controller.addPerson(cmd_args[0], str(cmd_args[1]))
            self.answer.make_privateMSG(context['user'])
            self.answer.set_text("add person " + cmd_args[0] + " r: " + str(cmd_args[1]))

        if cmd_stripped.startswith("p-"):
            #Usuń człowieka
            self.people_controller.removePerson(cmd_args[0])
            self.answer.make_privateMSG(context['user'])
            self.answer.set_text("remove person " + cmd_args[0])

        if cmd_stripped.startswith("f+"):
            #Dodaj fortunkę
            self.fortunes_controller.addFrotune(" ".join(cmd_args))
            self.answer.make_privateMSG(context['user'])
            self.answer.set_text("add fortune " + " ".join(cmd_args))

        if cmd_stripped.startswith("w+"):
            #Dodaj wiadomość powitalną
            self.welcomess_controller.addWelcomeMesage(" ".join(cmd_args))
            self.answer.make_privateMSG(context['user'])
            self.answer.set_text("add weclome msg " + " ".join(cmd_args))

        print "Komenda byl", cmd_name

    def getAnser(self):
        return self.answer
