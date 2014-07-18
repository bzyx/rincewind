'''
Created on 04-02-2013

@author: bzyx
'''
from rincewind.db.models import MasterAdmin
from rincewind.db import db


class Admin(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def addAdmin(self, name, username, role):
        m = MasterAdmin(name, username, role)
        db.save(m)
        db.commit()

    def validateAdmin(self, admin_name, username):
        m = db.get(MasterAdmin, name=admin_name)
        if m is None:
            return MasterAdmin.NOBODY
        else:
            if m.username == username:
                return m.role
            else:
                return MasterAdmin.NOBODY

    def removeAdmin(self, admin_name):
        m = db.get(MasterAdmin, name=admin_name)
        if m is not None:
            db.remove(m)
