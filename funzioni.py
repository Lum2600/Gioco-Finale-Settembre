import pygame, sys

class Flappy:
    def __init__(self, pos, size, screen) -> None:
        self.pos = pos
        self.size = size
        self.image = pygame.image.load("immagini\Fermo.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = pygame.Rect(self.pos, self.size)
        self.vel = [2, 2]
        self.muovimento_dx = False
        self.muovimento_sx = False
        self.muovimento_giu = False
        self.screen = screen
     
        self.salto = False


    def muovi_dx(self):
        self.muovimento_dx = True
    def muovi_sx(self):
        self.muovimento_sx = True
    
    def muovi_giu(self):
        self.muovimento_giu = True

    def muovi_su(self):
        self.muovimento_su = True


    def stop_dx(self):
        self.muovimento_dx = False
    def stop_sx(self):
        self.muovimento_sx = False
    def stop_su(self):
        self.muovimento_su = False
    def stop_giu(self):
        self.muovimento_giu= False



    def fermo(self, bole):
            if bole:
                self.vel = [0, 0]
            else: self.vel = [2, 2]

    def muovimento(self):
        
        if self.muovimento_dx:
            if not self.rect.right >= 100:
                self.rect.right += self.vel[0]
        if self.muovimento_sx:
            if not self.rect.left <=0:
                self.rect.right -= self.vel[0]
        if self.muovimento_giu:
            if not self.rect.top >= 300-self.size[1]:
                self.rect.top += self.vel[1]
        if self.muovimento_su:
            if not self.rect.top <=0:
                self.rect.top -= self.vel[1]


   
    def disegna(self, attacando,colpito ):
        if attacando:
            self.image= pygame.image.load("immagini\Attacco-removebg-preview.png")
        elif colpito:
            self.image= pygame.image.load("immagini\Colpito.png")        
        else:
            self.image= pygame.image.load('immagini\Fermo.png')


        self.image = pygame.transform.scale(self.image, self.size)
        self.screen.blit(self.image, self.rect)








#stessa cosa che hai fatto per le monete


        