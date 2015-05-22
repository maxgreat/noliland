# -*- coding: utf-8 -*-
"""
World API
@version: 0.1
@author: maxgreat


Contain class about land, case and world

"""
import ConfigParser
from debugOut import debug

class land(object):
    def __init__(self, filename):
        if type(filename) == str: self._openAndLoadFile(filename) 
        elif type(filename) == file: self._loadFile(filename) 
        else: raise (AttributeError, "Cannot open world with type "+ str(type(filename)))
        
    def _openAndLoadFile(self, filename):
        self._loadFile(open(filename, "r"))
    def _loadFile(self,f):
        self.map = []
        self.key = {}
        self.parser = ConfigParser.ConfigParser()
        parser.read(
        
#TODO : test if modifying a case after initializing, change the case in the land        

class case(object):
    def __init__(self,image,isCrossable,isInit):
        self.image=image
        self.isCrossable = isCrossable
        self.isInit = isInit

if __name__ == "__main__":
    print('Test of world package')
    a = land('data/lands/default1')
    print a