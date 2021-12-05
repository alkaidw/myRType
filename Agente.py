import pygame
from pygame.sprite import Sprite
from threading import Thread
from Colors import *
from Controller import Controller
import time
import Imagens
from Projetil import Projetil
from Missil import Missil

class Agente(Thread, Sprite):
    def __init__(self, tela, x, y, c):
        Thread.__init__(self)
        Sprite.__init__(self)
        self.display = tela.display
        self.controller = Controller(self,c)
        self.moving_x = 0
        self.moving_y = 0
        self.image = Imagens.nave1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = 0.001
        self.paused = False
        self.imunidade = False
        self.vida = 3
        self.imune = Imagens.imune
        self.listaDisparos = []

    def executeCommand(self, event):
        self.controller.execute(event)

    def draw(self):
        self.display.blit(self.image, (self.rect.x, self.rect.y))

    def setx(self, x):
        self.rect.x += x
        
    def sety(self, y):
        self.rect.y += y

    def run(self):
        while True:
            time.sleep(self.time)

            if self.rect.y < 0:
                self.rect.y = 0
            elif self.rect.y > 266:
                self.rect.y = 266
            elif self.rect.x < 4:
                self.rect.x = 4
            elif self.rect.x > 462:
                self.rect.x = 462
            
            if not self.imunidade or cont > 1000:
                cont = 0
                self.imunidade = False
                self.image = Imagens.nave1
                self.imune = Imagens.imune
            else:
                cont += 1
                
                if cont%50 == 0:
                    self.image, self.imune = self.imune, self.image

                
            self.setx(self.moving_x)
            self.sety(self.moving_y)
        pass

    def disparo(self):
        projetil = Projetil(self.display, self.rect.x, self.rect.y)
        self.listaDisparos.append(projetil)

    def missil(self):
        missil = Missil(self.display, self.rect.x, self.rect.y)
        self.listaDisparos.append(missil)

    def pause(self): 
        self.paused = True

    def unpause(self): 
        self.paused = False

    def batida(self):
        self.imunidade = True
        self.vida -= 1
        print("vida: ", self.vida)

    def gameOver(self):
        self.image = Imagens.gameOver
        print("GAME OVER")
        


