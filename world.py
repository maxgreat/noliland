# -*- coding: utf-8 -*-
"""
world v0.1

Contain class about land, case and world

"""
DEBUG=False

def debug(s):
    if(DEBUG):
        print(s)


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
        l = f.readline()        
        while l != '':
            if 'size' in l:
                size = f.readline().split(' ')
                self.height= int(size[0])
                self.width = int(size[1])
                debug('Size : ' + str(size))
            elif 'ground' in l and 'nb' in l:
                self.nbGrounds=int(f.readline())
            elif 'land' in l:
                for i in range(self.height):
                    line = f.readline().split(' ')
                    self.data.append([])                   
                    for j in range(self.width):
                        self.data[i].append(line[j])
                    #TODO : raise exception if the file is not correct
                debug('land'+str(self.data))
            l = f.readline()
                
        
        

class case(object):
    def __init__(self,image,passThrough):
        pass

if __name__ == "__main__":
    print('Test of world package')
    global DEBUG
    DEBUG=True
    a = land('data/lands/default1')