#prof sia clemente e si ricordi il progetto svolto durante l'anno
#e il fatto che su questo argomento ho preso l'unica sufficienza dell'anno
    

import pygame, sys
from funzioni import Flappy     
from pygame.locals import *
from random import randint
pygame.init()

WINDOW_SIZE = (500, 300)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('gioco')
screen.fill((0, 200, 0))


TIMERSHOT = pygame.event.custom_type()
pygame.time.set_timer(TIMERSHOT, 500)
incremento_al_sec= 1
 
sfondo = pygame.image.load("immagini\sfondo.png")
sfondo = pygame.transform.scale(sfondo, WINDOW_SIZE)

flappy = Flappy([0, WINDOW_SIZE[1]-50], (50, 50), screen)



lume_i1 = pygame.image.load('immagini\lume.png')
lume_i1 = pygame.transform.scale(lume_i1, (30, 30))
lume_r1 = pygame.Rect( (randint(600, 1000), randint(10, 250)), (30, 30) )



lume_i2 = pygame.image.load('immagini\lume.png')
lume_i2 = pygame.transform.scale(lume_i2, (30, 30))
lume_r2 = pygame.Rect( (randint(600, 1000), randint(100, 250)), (30, 30) )



lume_i3 = pygame.image.load('immagini\lume.png')
lume_i3 = pygame.transform.scale(lume_i3, (30, 30))
lume_r3 = pygame.Rect( (randint(600, 1000), randint(100, 250)), (30, 30) )



lumef_i1 = pygame.image.load('immagini\lume_forte.png')
lumef_i1 = pygame.transform.scale(lumef_i1, (30, 30))
lumef_r1 = pygame.Rect( (randint(600, 10000), randint(100, 250)), (30, 30) )


clock= pygame.time.Clock()
font = pygame.font.Font('fonts\ds_digital\DS-DIGI.TTF', 25)
#variaili varie
tempo = 0
vite = 5  
score = 0
vel_lume = 7             
n=1

while True:
    attacco = False
    colpito = False
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == TIMERSHOT:
            score+=incremento_al_sec
        
        
     
    keys =pygame.key.get_pressed()
            
    if keys[K_SPACE] and not keys[K_w] and not keys[K_s] and not keys[K_a] and not keys[K_d]:
                flappy.fermo(True)
                attacco = True
            
                


    lume_r1.x-=vel_lume
    if lume_r1.x < 0: 
                 lume_r1.x = randint(500, 700)
                 lume_r1.y = randint(10, 250)

    lume_r2.x-=vel_lume
    if lume_r2.x < 0: 
                 lume_r2.x = randint(500, 700)
                 lume_r2.y = randint(10, 250)

    lume_r3.x-=vel_lume
    if lume_r3.x < 0: 
                 lume_r3.x = randint(500, 700)
                 lume_r3.y = randint(10, 250)
    
    lumef_r1.x-=vel_lume
    if lumef_r1.x < 0: 
                 lumef_r1.x = randint(500, 700)
                 lumef_r1.y = randint(10, 250)
    
    

    if keys[K_d]:
         
                flappy.muovi_dx()
                flappy.fermo(False) 
    else:
                
                flappy.stop_dx()
                flappy.fermo(False)
    if keys[K_a]:
                flappy.muovi_sx()
                flappy.fermo(False)
    else:
                flappy.stop_sx()
                flappy.fermo(False) 
    if keys[K_w]:
                flappy.muovi_su()
                flappy.fermo(False)
    else:
             
                flappy.stop_su()
                flappy.fermo(False)
    if keys[K_s]:
                flappy.muovi_giu()
                flappy.fermo(False) 
    else:
                flappy.stop_giu()
                flappy.fermo(False)

     

    if flappy.rect.colliderect(lume_r1):
            if attacco:
                score+=10
                lume_r1.x = randint(600, 1000)
                lume_r1.y = randint(10, 250)
            else:
                vite-=1
                lume_r1.x = randint(600, 1000)
                lume_r1.y = randint(100, 250)

    if flappy.rect.colliderect(lume_r2):
            if attacco:
                score+=10
                lume_r2.x = randint(600, 1000)
                lume_r2.y = randint(100, 250)
            else:
                vite-=1
                lume_r2.x = randint(600, 1000)
                lume_r2.y = randint(100, 250)

    if flappy.rect.colliderect(lume_r3):
            if attacco:
                score+=10
                lume_r3.x = randint(500, 700)
                lume_r3.y = randint(100, 250)
            else:
                vite-=1
                lume_r3.x = randint(500, 700)
                lume_r3.y = randint(100, 250)

    if flappy.rect.colliderect(lumef_r1):
            
                    
            colpito = True
            lumef_r1.x = randint(500, 700)
            lumef_r1.y = randint(100, 250)
            if attacco:
                vite-=1
            else:
                vite-=2
    
    
        
                

#fai che se perrio il colpo torna indietro





    if vite == 5:
            vite_i = pygame.image.load("immagini\Vite-5-5.png")
            vite_i = pygame.transform.scale(vite_i, (100, 20))
    if vite == 4:
            vite_i = pygame.image.load("immagini\Vite-4-5.png")
            vite_i = pygame.transform.scale(vite_i, (100, 20))
    if vite == 3:
            vite_i = pygame.image.load("immagini\Vite-3-5.png")
            vite_i = pygame.transform.scale(vite_i, (100, 20))
    if vite == 2:
            vite_i = pygame.image.load("immagini\Vite-2-5.png")
            vite_i = pygame.transform.scale(vite_i, (100, 20))
    if vite == 1:
            vite_i = pygame.image.load("immagini\Vite-1-5.png")
            vite_i = pygame.transform.scale(vite_i, (100, 20))
    if vite<=0:
            break
    
            
    
    screen.blit(sfondo, (0,0))    
    screen.blit(lume_i3, lume_r3)
    screen.blit(lume_i2, lume_r2)
    screen.blit(lume_i1, lume_r1)
    screen.blit(lumef_i1, lumef_r1)
    screen.blit(vite_i, (10, 10))
    flappy.muovimento()
    flappy.disegna(attacco, colpito)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (400, 10))
    attacco = False
    colpito = False
            
            
            
    pygame.display.update()
    clock.tick(120)

