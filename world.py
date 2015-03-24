# -*- coding: utf-8 -*-
"""
World API
@version: 0.1
@author: maxgreat


Contain class about land, case and world

"""
from debugOut import debug
from kivy.uix.image import Image

class land(object):
    def __init__(self, filename):
        if type(filename) == str: self._openAndLoadFile(filename) 
        elif type(filename) == file: self._loadFile(filename) 
        else: raise (AttributeError, "Cannot open world with type "+ str(type(filename)))
        pass
    def _openAndLoadFile(self, filename):
        self._loadFile(open(filename, "r"))
    def _loadFile(self,f):
        self.data = []
        self.name = f.readline()[1:]
        debug('Name of the world : '+self.name)
        self.grounds=[];
        l = f.readline()        
        while l != '':
            if 'size' in l:
                size = f.readline().split(' ')
                self.height= int(size[0])
                self.width = int(size[1])
                debug('Size : ' + str(size))
            elif 'ground' in l and 'nb' in l:
                self.nbGrounds=int(f.readline())
            elif 'grounds' in l:
                for i in range(self.nbGrounds):
                    g = f.readline().split(' ')
                    self.grounds.append(case(g[0], bool(g[1])))
                #TODO : add exception if file is not correct
            elif 'land' in l:
                if len(self.grounds)==0:
                    debug('Grounds undefined before land reading')
                    exit(0)
                for i in range(self.height):
                    line = f.readline().split(' ')
                    self.data.append([])                   
                    for j in range(self.width):
                        self.data[i].append(self.grounds[int(line[j])])
                        #self.data[i].append(int(line[j]))
                    #TODO : raise exception if the file is not correct
                debug('land'+str(self.data))
            l = f.readline()
                
        
#TODO : test if modifying a case after initializing, change the case in the land        

class case(Image):
    def __init__(self,image,passThrough):
        Image.__init__(self, allow_stretch=True, keep_ratio=False)        
        self.image=image
        self.passThrough = passThrough

if __name__ == "__main__":
    print('Test of world package')
    global DEBUG
    DEBUG=True
    a = land('data/lands/default1')