import Imagens
import time
from Agente import Agente
from random import randint
from math import sin, pi, floor

class Inimigo(Agente):
    def __init__(self, tela, x, y, c, tipo=0):
        Agente.__init__(self, tela, x, y, c)        
        self.image = Imagens.inimigo1
        self.imageBackUp = Imagens.inimigo1
        self.inimigoMorto = False
        
        self.controller.setvelocity(randint(5,8))
        self.controller.setdirection(1)
        

    def run(self):
        respawnTime = 0
        while True:
            time.sleep(1/32)
            while self.paused:
                time.sleep(1)
                pass

            self.movimento()
            
            if self.inimigoMorto == True:
                respawnTime+=1

            if respawnTime == 30:
                respawnTime = 0
                self.inimigoMorto = False
                self.spawn()
                
        pass

    def collision(self, obj):
        if self.inimigoMorto == False:
            if self.rect.colliderect(obj.rect):
                return True
            else:
                return False

    def spawn(self):
        self.rect.x = randint(500,850)
        self.rect.y = randint(0,280)
        self.controller.setvelocity(randint(5,8))
        self.image = self.imageBackUp

    def morte(self):
        self.image = Imagens.explosao
        self.controller.velocity *= 0.28
        self.inimigoMorto = True

    def movimento(self):
        self.setx(-1 * self.controller.velocity)
        self.sety(0)

        
class Inimigo2(Inimigo):
    def __init__(self, tela, x, y, c, tipo=0):
        Inimigo.__init__(self, tela, x, y, c)
        self.image = Imagens.inimigo2
        self.imageBackUp = Imagens.inimigo2
        self.f=randint(10,60)
        self.s=randint(10,310)

    def movimento(self):
        self.setx(-1 * self.controller.velocity)
        self.rect.y = sin(self.rect.x/100)*self.f + self.s



##    def mov1(self):
##            self.x += self.velocidade()
##            self.y = sin(self.x/10)*self.f + self.s
##            print(self.x,self.y)
##
##    def velocidade(self):
##        print(floor(self.vel / (self.f*0.169))+1*self.sentidox, self.f*0.169)
##        return floor(self.vel / (self.f*0.169))+1*self.sentidox        
