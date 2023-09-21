#Use Pygame to draw a black sreen
import os
import pygame
import sys
from pygame.locals import *
import config
import cursor
import grave
import zombie
import random

WIDTH =1080
HEIGHT = 700
pygame.init()


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Zombie Smash")
clock=pygame.time.Clock()
cursor=cursor.Cursor()
back_ground=pygame.image.load(os.path.join(config.image_folder,"bg2.jpg")).convert_alpha()
back_ground=pygame.transform.scale(back_ground,(WIDTH,HEIGHT))
game_over=pygame.image.load(os.path.join(config.image_folder,"game_over.jpg")).convert_alpha()
menu=pygame.image.load(os.path.join(config.image_folder,"menu.png")).convert_alpha()
#Load the grave image
Grave=grave.grave()

#Load the zombie image
zombie_list=[]
zombie_list.append(zombie.zombie(Grave.rect[0],195,195))
zombie_list.append(zombie.zombie(Grave.rect[1],90,90, 1))
zombie_list.append(zombie.zombie(Grave.rect[2],87,87))
zombie_list.append(zombie.zombie(Grave.rect[3],195,195))
zombie_list.append(zombie.zombie(Grave.rect[4],66,66))

def random_zombie():
    return random.choice(zombie_list)
    

#Game init
def game_init():
    #init global variable
    global timer
    timer=30
    global score
    score =0
    global Zombie
    Zombie=random_zombie()
    global miss
    miss=0
    global escaped
    escaped=0
    global is_hit
    is_hit=0
    global Zombie_time
    Zombie_time=90*2.4
    global game_status
    game_status =1
    Zombie.current_image=Zombie.image[0]


#add background music
pygame.mixer.music.load(os.path.join(config.image_folder,"bgm.mp3"))
pygame.mixer.music.play(-1, 0.0)




smash_sfx=pygame.mixer.Sound(os.path.join(config.image_folder,"smash_sfx.mp3"))
zombie_sfx=pygame.mixer.Sound(os.path.join(config.image_folder,"zombie_sfx.mp3"))
btn_click_sfx=pygame.mixer.Sound(os.path.join(config.image_folder,"btn_click.mp3"))

game_init()
game_status=-1
while True:
    if(timer<=0):
        game_status=0
    if(game_status==-1):
        #menu game
        screen.fill((0,0,0))
        screen.blit(menu,(182.5,80))
        #play and quit button
        Play_color=(255,255,255)
        font_path=os.path.join(config.font_folder,"prstart.ttf")
        font=pygame.font.Font(font_path, 60)
        text=font.render("Press Start!",True,Play_color)
        screen.blit(text,(220,487))
        button_rect=pygame.Rect(210,460,720,100)
        #draw button
        #pygame.draw.rect(screen,(255,255,255),button_rect,1)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                cursor.onClick()
                print(pygame.mouse.get_pos())
                if(button_rect.collidepoint(pygame.mouse.get_pos()) and game_status==-1):
                    #play button click sound
                    btn_click_sfx.play()
                    #wait for sound to finish
                    pygame.time.wait(700)
                    game_init()
                    
            elif event.type==MOUSEBUTTONUP:
                cursor.onRelease()

    if(game_status==0):
        screen.fill((0,0,0))
        screen.blit(game_over,(25,0))
        #print score, miss, escaped in middle of screen
        Play_again_color=(255,255,255)
        font_path=os.path.join(config.font_folder,"prstart.ttf")
        font=pygame.font.Font(font_path, 60)
        text=font.render("Play Again",True,Play_again_color)
        screen.blit(text,(260,600))
        button_rect=pygame.Rect(240,580,620,90)
        #draw button
        #pygame.draw.rect(screen,(255,255,255),button_rect,1)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                cursor.onClick()
                if(button_rect.collidepoint(pygame.mouse.get_pos()) and game_status==0):
                    btn_click_sfx.play()
                    pygame.time.wait(700)
                    game_init()
            elif event.type==MOUSEBUTTONUP:
                cursor.onRelease()
        font_path=os.path.join(config.font_folder,"prstart.ttf")
        font=pygame.font.Font(font_path, 40)
        text=font.render("Score:   "+str(score),True,(255,255,255))
        screen.blit(text,(WIDTH/2-180,HEIGHT/2+50))
        text=font.render("Miss:    "+str(miss),True,(255,255,255))
        screen.blit(text,(WIDTH/2-180,HEIGHT/2+100))
        text=font.render("Escaped: "+str(escaped),True,(255,255,255))
        screen.blit(text,(WIDTH/2-180,HEIGHT/2+150))
        #Play again button

        
        

      
        
    if(game_status==1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                cursor.onClick()
            #check collision
                if(Zombie.status==1 and Zombie.rect.collidepoint(pygame.mouse.get_pos()) and game_status==1): #if collide
                #play smash sound
                    smash_sfx.play()
                    Zombie_time=30*2.4
                    Zombie.current_image=Zombie.image[1]
                    score+=1
                    is_hit=1
                else:
                    if(game_status==1):
                        miss+=1
                
            elif event.type==MOUSEBUTTONUP:
                cursor.onRelease()
    
        timer-=1/144

        screen.fill((0,0,0))
        screen.blit(back_ground,(0,0))
        #print score
        font_path=os.path.join(config.font_folder,"prstart.ttf")
        font=pygame.font.Font(font_path, 20)
        text=font.render("Score:   "+str(score),True,(255,255,255))
        screen.blit(text,(10,10))
        text=font.render("Miss:    "+str(miss),True,(255,255,255))
        screen.blit(text,(10,40))
        text=font.render("Escaped: "+str(escaped),True,(255,255,255))
        screen.blit(text,(10,70))
        #print timer
        font_path=os.path.join(config.font_folder,"prstart.ttf")
        font=pygame.font.Font(font_path, 40)
        timer_color=(255,255,255)
        if(timer<=10):
            timer_color=(255,0,0)
        text=font.render(str(int(timer)),True,timer_color)
        screen.blit(text,(WIDTH/2-25,30))

        #Update Zombie Logic
        if(Zombie.status==0 and game_status==1):
            Zombie.rect.y-=10
            if(Zombie.rect.y<=Zombie.filnal_pos_y):
                Zombie.status=1
                zombie_sfx.play()
        elif(Zombie.status==1 and game_status==1):
            Zombie_time-=1
            if(Zombie_time<=0):
                Zombie.status=2
                
        elif(Zombie.status==2 and game_status==1):
            Zombie.rect.y+=10
            if(Zombie.rect.y>=Zombie.init_pos):
                Zombie.rect.y=Zombie.init_pos
                if(is_hit==0):
                    escaped+=1
                Zombie.current_image=Zombie.image[0]
                Zombie_time=90*2.4
                Zombie=random_zombie()
                is_hit=0
                Zombie.status=0
                #play zombie sound
        
   
        
        screen.blit(Zombie.current_image,Zombie.rect)
        for i in range(0,5):
            #pygame.draw.circle(screen,(255,0,0),(Grave.location[i][0]+50, Grave.location[i][1]+50),20)
            screen.blit(Grave.image[i],Grave.location[i])
            #pygame.draw.rect(screen,(255,0,0),Grave.rect[i],1)
    cursor.update()
    cursor.draw(screen)
    
    pygame.display.update()
    clock.tick(144)
