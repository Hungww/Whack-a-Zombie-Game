import config
import pygame
import os
import sys
from pygame.locals import *
class grave():
    def __init__(self):
        self.image=[None,None,None,None,None]
        self.rect=[None,None,None,None,None]
        for(i) in range(0,5):
            self.image[i]=pygame.image.load(os.path.join(config.image_folder,"grave"+str(i+1)+".png")).convert_alpha()
            self.rect[i]=self.image[i].get_rect()
            
        self.location=[None,None,None,None,None]

        self.location[0]=(190,427)
        self.rect[0].x=self.location[0][0]
        self.rect[0].y=self.location[0][1]


        self.location[1]=(485,349)
        self.rect[1].x=self.location[1][0]
        self.rect[1].y=self.location[1][1]


        self.location[2]=(737,317)
        self.rect[2].x=self.location[2][0]
        self.rect[2].y=self.location[2][1]


        self.location[3]=(878,550)
        self.rect[3].x=self.location[3][0]
        self.rect[3].y=self.location[3][1]

        self.location[4]=(896,305)
        self.rect[4].x=self.location[4][0]
        self.rect[4].y=self.location[4][1]



            

