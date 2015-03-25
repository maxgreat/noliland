# -*- coding: utf-8 -*-
"""
World API
@version: 0.1
@author: maxgreat


Contain class about land, case and world

"""
from debugOut import debug

class land(object):
    def __init__(self, filename):
        if type(filename) == str: self._openAndLoadFile(filename) 
        elif type(filename) == file: self._loadFile(filename) 
        else: raise (AttributeError, "Cannot open world with type "+ str(type(filename)))
        
    def _openAndLoadFile(self, filename):
        self._loadFile(open(filename, "r"))
    def _loadFile(self,f):
        #every variable to init
        self.data = []
        self.height=0
        self.width=0
        self.nbGrounds=0
        self.grounds=[];
        self.name = f.readline()[1:]
        debug('Name of the world : '+self.name)
        
        l = f.readline()        
        while l != '':
            if 'size' in l: #initialize the size of the map
                size = f.readline().split(' ')
                self.height= int(size[0])
                self.width = int(size[1])
                debug('Size : ' + str(size))
                
            elif 'nb' in l and 'ground' in l: #initialize the number of different ground
                self.nbGrounds=int(f.readline())
                self.grounds=[[]]*self.nbGrounds
                
            elif 'grounds' in l: #read the different grounds
                self.textureFile=f.readline()[:-1]
                try:
                    for i in range(self.nbGrounds):
                        g = f.readline().split(' ')
                        self.grounds[int(g[0])] = case(map(int,g[1:5]), bool(g[5]), g[5]=='2')
                except:
                    raise
                    
            elif 'land' in l: #read the map
                if len(self.grounds)==0:
                    debug('Grounds undefined before land reading')
                    raise Exception('ReadMapFailure','Grounds not initlized before reading map')
                self.data=[[]]*self.height
                for i in range(self.height):
                    line = f.readline().split(' ')
                    self.data[i] = [[]]*self.width                 
                    for j in range(self.width):
                        self.data[i][j] = int(line[j])
                        #self.data[i].append(int(line[j]))
                    #TODO : raise exception if the file is not correct
                debug('land'+str(self.data))
            l = f.readline()
         #end reading file   
            
        if(len(self.data)==0 or self.width==0 or self.height==0 or self.nbGrounds==0 or len(self.grounds)==0):
            debug('Error reading the map file')
            raise Exception('ReadMapFailure','Error in the map file') #TODO : different error for each failure
        
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