import config
import pygame
import os
import sys

class zombie():
    def __init__(self, Grave_Rect, width, height, left_flag=0):
        self.image=[None,None]
        self.image[0]=pygame.image.load(os.path.join(config.image_folder,"zombie_idle.png")).convert_alpha()
        self.image[0]=pygame.transform.scale(self.image[0],(width,height))
        self.image[1]=pygame.image.load(os.path.join(config.image_folder,"zombie_hurt.png")).convert_alpha()
        self.image[1]=pygame.transform.scale(self.image[1],(width,height))
        self.current_image=self.image[0]
        self.rect=self.image[0].get_rect()
        self.rect.midtop=Grave_Rect.midtop
        self.init_pos=Grave_Rect.y
        self.filnal_pos_y=Grave_Rect.midtop[1] - self.rect.height*0.7
       
        
        self.status=0


    
