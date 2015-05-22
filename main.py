# -*- coding: utf-8 -*-
"""
Created on Tue May 22 2015

@author: maxgreat
"""

GRAPHICS=True #False if we don't use kivy or pygame yet

import world
from living import Player
from debugOut import debug

def drawWorld(m): #only for debug
    if GRAPHICS:
        pass
    else:
        for i in range(m.height):
            for j in range(m.width):
                #for now it's debug --> Only work with python 2
                print '1' if m.data[i][j].image == 'default1.jpg' else '2' ,
            print(' ')
            
#cast value in the given interval
def castInterval(interval, value):
        return min([ interval[1], max([ interval[0], value]) ])


            
 #charge the default land      
SCREEN_SIZE_W = 255
SCREEN_SIZE_H = 255


class game(object):
    def __init__(self, land='data/lands/default2'):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE_W,SCREEN_SIZE_H)) #TODO : verify order
        self.screen.fill((255, 255, 255)) #fill the screen in white -> not useful
        self.MAP=world.land('data/lands/default.map')



if __name__ == "__main__":

