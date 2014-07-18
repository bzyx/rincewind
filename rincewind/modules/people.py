'''
Created on 04-02-2013

@author: bzyx
'''
from rincewind.db import db
from rincewind.db.models import Person


class PeopleManager(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def addPerson(self, name, role):
        p = Person(name, role)
        db.save(p)
        db.commit()

    def removePerson(self, nameP):
        p = db.load(Person, name=nameP)
        if p is not None:
            db.remove(p)
            db.commit()

    def deleteAllPeople(self):
        people = db.load(Person)
        for p in people:
            db.remove(p)
        db.commit()

    def countAllPeople(self):
        people = db.load(Person)
        return len(people)

    def getPeopleForRole(self, roleName):
        people = db.load(Person, type=roleName)
        people_names = [p.name for p in people]
        return people_names
