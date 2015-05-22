# -*- coding: utf-8 -*-
"""
Created on Tue May 22 2015

@author: maxgreat
"""

GRAPHICS=True #False if we don't use kivy or pygame yet

import pygame
from pygame.locals import *
import world
from living import Player
from debugOut import debug

       
SCREEN_SIZE_W = 255
SCREEN_SIZE_H = 255
FPS = 15
NB_TILE_SCREEN_W = 5
NB_TILE_SCREEN_H = 5

#Colors
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

class engine(object):
    """
    Big handler for pygame rendering
    Handle the map from world.py
    """
    def __init__(self, land='data/lands/default1.map'):
        """
        Init Engine instance - by default load the map default1
        """
        pygame.init()
        self.world=world.land('data/lands/default1.map')
        self.screen = pygame.display.set_mode((self.world.TILE_WIDTH*NB_TILE_SCREEN_W, self.world.TILE_HEIGHT*NB_TILE_SCREEN_H)) #TODO : verify order
        self.screen.fill((255, 255, 255)) #fill the screen in white -> not useful
        self.game_ended = False
        print 'Try to open image : ', self.world.maptexture
        self.tilesetImage = pygame.image.load(self.world.maptexture)
        
    def render(self):
        """
        Render the scene
        """
        w = self.world
        for i in range(NB_TILE_SCREEN_W):
            for j in range(NB_TILE_SCREEN_H):
                c = w.cases[w.map[i][j]]
                image = self.tilesetImage.subsurface(c.tile[0]*w.TILE_WIDTH, c.tile[1]*w.TILE_HEIGHT,w.TILE_WIDTH,w.TILE_HEIGHT)
                #self.screen.blit(image, (i*w.TILE_WIDTH, j*w.TILE_HEIGHT))
                self.screen.blit(image, (0, 0))
        
    def event_handler(self):
        """
        Handle user event
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.game_ended = True
            elif event.type == pygame.locals.KEYDOWN:
                self.pressed_key = event.key
    
    def game_over(self):
        """
        Return engine state
        """
        return self.game_ended

if __name__ == "__main__":
    game = engine()
    clock = pygame.time.Clock() #use to limit FPS
    while not game.game_over():
        game.event_handler() #handle user event
        game.render()        #render scene
        clock.tick(FPS)      #wait to limit FPS
    print 'Game Ended Properly'
