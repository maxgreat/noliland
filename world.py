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
        if type(filename) == str: self._loadFile(filename) 
        else: raise (AttributeError, "Cannot open world with type "+ str(type(filename)))
        
    def _openAndLoadFile(self, filename):
        self._loadFile(open(filename, "r"))
    def _loadFile(self,filename):
        self.cases = {}
        parser = ConfigParser.ConfigParser()
        parser.read(filename)
        self.maptexture = parser.get("level", "maptexture")
        self.map = [i.split(' ') for i in parser.get("level", "map").split('\n')]
        
        self.TILE_WIDTH = int(parser.get("tiledata","tile_width"))
        self.TILE_HEIGHT = int(parser.get("tiledata","tile_height"))
        
        for section in parser.sections():
            if len(section) <= 2:
                print 'Section ', section
                desc = dict(parser.items(section))
                self.cases[section] = case(desc)

class case(object):
    def __init__(self,state):
        for s in state:
            if s == 'name':
                self.name = state[s]
            elif s == 'tile':
                self.tile = [int(i) for i in state[s].split(',')]
            elif s == 'blockWalk':
                self.walk = False
            elif s == 'blockFly':
                self.fly = False
            elif s == 'sprite':
                self.sprite = True
                self.image = state[s]
                

if __name__ == "__main__":
    print('Test of world package')
    a = land('data/lands/default1.map')
    print a