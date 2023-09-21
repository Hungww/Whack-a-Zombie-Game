import config
import pygame
import os
import sys
from pygame.locals import *

class Cursor(pygame.Rect):
    def __init__(self):
        self.image=[None,None]
        self.image[0]=pygame.image.load(os.path.join(config.image_folder,"cursor0.png")).convert_alpha()
        self.image[1]=pygame.image.load(os.path.join(config.image_folder,"cursor1.png")).convert_alpha()
        self.image[0]=pygame.transform.scale(self.image[0],(230,230))
        self.image[1]=pygame.transform.scale(self.image[1],(230,230))

        self.current_image=0
        self.CursorRect=self.image[0].get_rect()
        #make default cursor invisible
        pygame.mouse.set_visible(False)
    def update(self):
        self.CursorRect.center=pygame.mouse.get_pos()
        self.CursorRect.x+=40
        self.CursorRect.y+=10
        self.x=pygame.mouse.get_pos()[0]
        self.y=pygame.mouse.get_pos()[1]
    def draw(self,screen):
        screen.blit(self.image[self.current_image],self.CursorRect)
       
    def onClick(self):
        self.current_image=1
    def onRelease(self):
        #delay 0.2 seconds
        pygame.time.delay(50)
        self.current_image=0