# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:26:25 2015

@author: maxgreat
"""
from kivy.app import App
from kivy.core.image import Image
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle, Ellipse
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
            
            
MAP=world.land('data/lands/default2') #charge the default land      


#GRID=[]
#def gridImages():
#    global GRID
#    global MAP
#    GRID = []
#    for i in range(10):
#        GRID.append([])
#        for j in range(10):
#            #g[i].append(Image(source='data/'+m.data[i][j]))
#            GRID[i].append(Image(source='data/images/'+MAP.data[i][j].image,allow_stretch=True, keep_ratio=False))
#            #g[i].append(m.grounds[m.data[i][j]])  

class MyWorld(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.nbCases=10
        #initialize the player
        dataPerso = {'position':[5,5],'health':10,'name':'LittlePlayer'}
        self.player=Player(dataPerso)
        global MAP
        debug('Texture:'+MAP.textureFile)
        self.texture=Image('data/images/'+MAP.textureFile).texture
        self.drawImages
    def update(self,dt):
        self.drawImages()


    def on_touch_down(self,touch):
        #TODO : BUG
        newTouch=[touch.x/self.nbCases, touch.y/self.nbCases]
        print 'Touch :', touch.pos
        print 'NewTouch :',newTouch
        print 'Player:', self.player.position
        if newTouch[0] < self.player.position[0]:
            self.player.position[0] -= 1
        elif newTouch[0] > self.player.position[0]:
            self.player.position[0] += 1

    def drawImages(self):
        global MAP
        size=[self.size[0]/self.nbCases, self.size[1]/self.nbCases]
        self.player.size=size
        tex = [[]]*MAP.nbGrounds
        for i in range(MAP.nbGrounds):
            grid = MAP.grounds[i].image
            tex[i] = self.texture.get_region(grid[0], grid[1], grid[2], grid[3])
        with self.canvas:
            for i in range(self.nbCases):
                for j in range(self.nbCases):
                    posOnScreen=[i*size[0],j*size[1]]
                    posOnMap=[min([MAP.height-1,max([0,self.player.position[0]-i+self.nbCases/2])]), min([MAP.width-1,max([0,self.player.position[1]-j+self.nbCases/2])])]
                    debug('PosOnMap:'+str(posOnMap))
                    Rectangle(texture=tex[MAP.data[posOnMap[0]][posOnMap[1]]], pos=posOnScreen, size=size)
            Ellipse(pos=[size[0]*self.nbCases/2,size[1]*self.nbCases/2],size=size)
        #with self.player.canvas:
        #    Ellipse(pos=self.pos, size=self.size)
#class NoLiGame(GridLayout):
#    def __init__(self):  
#        GridLayout.__init__(self,cols=10,rows=10)
#        self.call = 0
#        self.reverse=True
#        global GRID
#        for i in range(10):
#            for j in range(10):
#                self.add_widget(GRID[i][j])                
#    def update(self,dt):
#        pass

class NoLiApp(App):
    def build(self):
#        gridImages()
#        game = NoLiGame()
        game = MyWorld()
        Clock.schedule_interval(game.update, 1.0 / 30.0)
        return game

if __name__ == "__main__":
    NoLiApp().run()
    #drawWorld(map1)

