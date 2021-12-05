from threading import Thread
import pygame
from pygame import locals
from pygame.locals import *
from Projetil import Projetil
from Missil import Missil


class Controller:
    
    def __init__(self, obj, type=1):        
        self.obj = obj
        self.velocity = 1
        self.direction = 1


        self.up = False
        
        if type == 1:
            self.K_UP = K_UP
            self.K_DOWN = K_DOWN
            self.K_LEFT = K_LEFT
            self.K_RIGHT = K_RIGHT
            self.K_SPACE = K_SPACE
            self.K_m = K_m
        else:
            self.K_UP = K_w
            self.K_DOWN = K_s
            self.K_LEFT = K_a
            self.K_RIGHT = K_d
            self.K_SPACE = K_SPACE
            self.K_m = K_m

        
    def setvelocity(self, v=1):
        self.velocity = v

    def setdirection(self, d=1):
        self.direction = d


    def execute(self, event):
        print(self.obj.rect.x, self.obj.rect.y)
        key = event.key

        if event.type == KEYDOWN:
                        
            if key==self.K_UP:
                self.up = True
                self.obj.moving_y = (-self.direction * self.velocity)
                
            elif key==self.K_DOWN and self.up == False:
                self.obj.moving_y = (self.direction * self.velocity)
                            
            elif key==self.K_LEFT:
                self.obj.moving_x = (-self.direction * self.velocity)
                            
            elif key==self.K_RIGHT:
                self.obj.moving_x = (self.direction * self.velocity)
                
            elif key==self.K_SPACE:
                self.obj.disparo()

            elif key==self.K_m:
                self.obj.missil()


        elif event.type == KEYUP:
            
            if key==self.K_UP:
                self.up = False
                self.obj.moving_y = 0

            elif key==self.K_DOWN:
                self.obj.moving_y = 0
                            
            elif key==self.K_LEFT:
                self.obj.moving_x = 0
                            
            elif key==self.K_RIGHT:
                self.obj.moving_x = 0

        
