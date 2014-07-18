# -*- coding: utf-8 -*-
'''
Created on 03-02-2013

@author: bzyx
'''
import minidb


class MasterAdmin(object):
    SUPER_ADMIN = 0
    CAN_ADD_FORTUNE = 100
    NOBODY = 1000
    __slots__ = {'name': str, 'username': str, 'role': int}

    def __init__(self, name, username, role=NOBODY):
        self.name = name
        self.username = username
        self.role = role


class FortuneModel(object):
    __slots__ = {'text': unicode}

    def __init__(self, text):
        self.text = text


class WelcomeMsgModel(object):
    __slots__ = {'text': unicode}

    def __init__(self, text):
        self.text = text


class Person(object):
    __slots__ = {'name': str, 'type': str}

    def __init__(self, name, type):
        self.name = name
        self.type = type