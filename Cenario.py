import pygame
from threading import Thread
from random import randint
from Imagens import *
import time

class Cenario(Thread):

    def __init__(self, tela):
        Thread.__init__(self)
        self.display = tela.display

    def draw(self):
        self.display.blit(bg1, (int(self.i), self.h1))
        self.display.blit(bg1, (int(self.j), self.h2))

        self.display.blit(bg3, (int(self.k), self.h3))
        self.display.blit(bg3, (int(self.l), self.h4))

    def run(self):
        self.i = 960
        self.j = 0
        self.k = 960
        self.l = 0
        self.h1 = randint(-320,0)
        self.h2 = randint(-320,0)
        self.h3 = randint(-320,0)
        self.h4 = randint(-320,0)
        
        while True:
            time.sleep(.007) #quanto menor, mais rápido o fundo passa
            #acrescenta o bg1
            if self.i < -960:
                self.i = 960
                self.h1 = randint(-320, 0)

            if self.j < -960:
                self.j = 960
                self.h2 = randint(-320, 0)

            #acrescenta o bg3
            if self.k < -960:
                self.k = 960
                self.h3 = randint(-320, 0)

            if self.l < -960:
                self.l = 960
                self.h4 = randint(-320, 0)


##            self.display.blit(bg1, (int(i), h1))
##            self.display.blit(bg2, (int(j), h2))
##
##            self.display.blit(bg3, (int(k), h3))
##            self.display.blit(bg4, (int(l), h4))

            self.i-=1
            self.j-=1
            self.k-=2
            self.l-=2
