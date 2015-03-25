# -*- coding: utf-8 -*-
"""
Living things API
@version: 0.1
@author: maxgreat
"""

from debugOut import debug

#from kivy.uix.widget import Widget

class LivingThing(object):
    def __init__(self, data={}):
        if len(data)==0:
            debug('Cannot initialize that living thing')
            raise Exception('ErrorInitLiving', 'Data for Living thing empty')
        try:
            self.position=data['position']
            self.health=data['health']
            self.name=data['name']
        except:
            raise
        pass
    def hit(self,strength):
        debug(self.name + ' hit by strengh : ' + str(strength)  )      
        self.health -= strength
    def isDead(self):
        debug('Is Dead:'+str(self.health <= 0))
        return self.health <= 0
    def move(self,movement):
        debug('Move : '+str(movement))
        self.position[0] += movement[0]
        self.position[1] += movement[1]

class Player(LivingThing):
    def __init__(self,data):
        LivingThing.__init__(self,data)

class PnG(LivingThing):
    def __init__(self,data):
        LivingThing.__init__(self,data)

if __name__ == "__main__":
    print('Test of livingThing package')
    dataPerso = {'position':[0,0],'health':10,'name':'LittlePlayer'}
    a = LivingThing(dataPerso)
    a.hit(5)
    a.move([-1,0])
    a.hit(10)
    a.isDead()
