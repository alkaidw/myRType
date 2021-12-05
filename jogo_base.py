import pygame
import time
from pygame.sprite import Group
from random import randint
from Colors import *
from Fontes import *
from Display import *
from Agente import Agente
from Controller import *
import Imagens
from Cenario import *
from Inimigo import Inimigo, Inimigo2


class Game:
    def __init__(self):
        self.agentes = []
        self.frame_rate = 30
        
    def start(self):
        pass

frame_rate = 30
fonte = pygame.font.get_default_font()
fonteJogo = pygame.font.SysFont("harlowsolid", 60)


def main():
    pygame.init()

    tela = Display(500, 300, "jogo base")
    pygame.display.set_icon(gameIcon)
    relogio = pygame.time.Clock()
    relogio.tick(2)

    cenario = Cenario(tela)
    cenario.start()

    sair = False

    inimigos = []
    tiposDeInimigo = [Inimigo, Inimigo, Inimigo, Inimigo2]
    for i in range(4):
        inimigo = tiposDeInimigo[randint(0,3)](tela, randint(500,850), randint(0,280), 0)
        inimigos.append(inimigo)
        inimigo.start()

    nave = Agente(tela, 120, 120, 0)
    nave.controller.setvelocity(1)
    nave.controller.setdirection(1)
    nave.start()

    g = Group(nave)
    
    
    while not sair:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.KEYDOWN or\
                event.type == pygame.KEYUP:
                nave.executeCommand(event)

            if event.type == pygame.KEYDOWN:
                if event.key == K_p:
                    if not inimigo.paused:
                        inimigo.pause()
                    else:
                        inimigo.unpause()

        for inimigo in inimigos:        
            if inimigo.collision(nave) and nave.imunidade == False:
                nave.batida()
            
        if nave.vida < 1:
            
            break
        
        tela.fill(black)

        for tiro in nave.listaDisparos:
            tiro.draw()
            tiro.movimento()

            for inimigo in inimigos:
                if inimigo.collision(tiro):
##                    inimigos.remove(inimigo)
                    inimigo.morte()
                    nave.listaDisparos.remove(tiro)
            
            if tiro.rect.x > 475:
                nave.listaDisparos.remove(tiro)

        for inimigo in inimigos:
            if inimigo.rect.x <= 0:
                inimigo.spawn()
                print(inimigo.rect.x)
                

        cenario.draw()

        for inimigo in inimigos:
            inimigo.draw()
        
        g.draw(tela.display)
       
        pygame.display.update()


    nave.gameOver()
    nave.draw()
    text = fonteJogo.render("Game Over", 1, color)
    tela.display.blit(text,(120,101))
    pygame.display.update()
    time.sleep(2)
    
    nave.image = Imagens.explosao
    nave.draw()
    pygame.display.update()
    time.sleep(6)

    
    pygame.quit()


main()
