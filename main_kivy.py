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
from kivy.core.window import Window #for keyboard input
from kivy.core.text import Label as CoreLabel

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
        
        #KeyBoard handling
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        
        self.nbCases=15 #nb Case to draw on screen
        #initialize the player
        dataPerso = {'position':[5,5],'health':10,'name':'LittlePlayer'} #should depend on the map
        self.player=Player(dataPerso)

        global MAP
        debug('Texture:'+MAP.textureFile)
        self.texture=Image('data/images/'+MAP.textureFile).texture #load texture for the map
        self.tex = [[]]*MAP.nbGrounds
        for i in range(MAP.nbGrounds):
            grid = MAP.grounds[i].image
            self.tex[i] = self.texture.get_region(grid[0], grid[1], grid[2], grid[3])
        
        self.drawImages
        
    def update(self,dt): #for each frame
        self.drawImages()


    #TODO for android !
    # def on_touch_down(self,touch): #touch on the screen
        # #TODO : BUG
        # newTouch=[touch.x/self.nbCases, touch.y/self.nbCases]
        # print 'Touch :', touch.pos
        # print 'NewTouch :',newTouch
        # print 'Player:', self.player.position
        # if newTouch[0] < self.player.position[0]:
            # self.player.position[0] -= 1
        # elif newTouch[0] > self.player.position[0]:
            # self.player.position[0] += 1

    def _keyboard_closed(self):
        debug('Keyboard have been closed')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

        
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        #TODO : a table to store every key, boolean for pressed or not
        if keycode[1] == 'up' and self.player.position[0] < MAP.height-1: #&& self.canDoUp:
            self.player.move([1,0])
        elif keycode[1] == 'down' and self.player.position[0] > 1:
            self.player.move([-1,0])
        elif keycode[1] == 'left' and self.player.position[1] > 1 : 
            self.player.move([0,-1])
        elif keycode[1] == 'right' and self.player.position[1] < MAP.width-1:
            self.player.move([0,1])
        else:
            return False
        return True
        
    def drawImages(self): #draw the map
        global MAP
        sizeOfCase=[self.size[0]/self.nbCases, self.size[1]/self.nbCases] #Careful : width then height
        self.player.size=sizeOfCase
        
        with self.canvas:
            for line in reversed(range(self.nbCases)):
                for col in range(self.nbCases):
                    
                    posOnScreen=[col*sizeOfCase[0],line*sizeOfCase[1]] #width then height
                    #debug('Position on screen'+str(posOnScreen))
                    posOnMap={}
                    posOnMap['width']= castInterval( [0,MAP.width-1], self.player.position[1]-col+self.nbCases/2)
                    posOnMap['height']= castInterval( [0,MAP.height-1], self.player.position[0]-line+self.nbCases/2)
                    #debug('Position Player:'+str(self.player.position))
                    #debug('Position on map'+str(posOnMap))
                    
                    #add for debug
                    my_label = CoreLabel()
                    my_label.text = str(posOnMap['width']) + ':' + str(posOnMap['height'])
                    my_label.padding = 30.0
                    my_label.refresh()
                    
                    Rectangle(texture=self.tex[MAP.data[posOnMap['height']][posOnMap['width']]], pos=posOnScreen, size=sizeOfCase)
                    Rectangle(texture=my_label.texture,  pos=posOnScreen, size=sizeOfCase)
            Ellipse(pos=[ (sizeOfCase[0]*self.nbCases+sizeOfCase[0])/2 , (sizeOfCase[1]*self.nbCases+sizeOfCase[1])/2],size=sizeOfCase) #drawPlayer


class NoLiApp(App):
    def build(self):
        game = MyWorld()
        Clock.schedule_interval(game.update, 1.0 / 30.0)
        return game

if __name__ == "__main__":
    NoLiApp().run()
    #drawWorld(map1)
