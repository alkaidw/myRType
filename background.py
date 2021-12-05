import pygame
from random import randint
## cores
cor_branco = (255,255,255)
preto = (0,0,0)


def main():
    #inicializa o pygame
    pygame.init()

    #define a tela
    tela = pygame.display.set_mode([480, 320])


    gameIcon = pygame.image.load("sprites/icon.png")
    pygame.display.set_icon(gameIcon)
    
    #pygame.set_caption("jogao", icontitle=None)
    #define o titulo na barra

    #pygame.display.set_caption("exemplo background")
    #define o clock (frame rate)
    relogio = pygame.time.Clock()
    
    #define o background
    bg1 = pygame.image.load("sprites/fundo1.png")
    bg2 = pygame.image.load("sprites/fundo1.png")
    bg3 = pygame.image.load("sprites/fundo2.png")
    bg4 = pygame.image.load("sprites/fundo2.png")


    #bg2 = pygame.image.load("fundo2.png")

    #loop principal
    sair = False
    i = 960
    j = 0
    k = 960
    l = 0
    h1 = randint(-320,0)
    h2 = randint(-320,0)
    h3 = randint(-320,0)
    h4 = randint(-320,0)
    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            #if event.type == pygame.KEYDOWN



        #ajusta framerate, quadros por segundo                
        relogio.tick(60)

        
        tela.fill((0,0,0))

        #acrescenta o bg
        if i < -960:
            i = 960
            h1 = randint(-320, 0)

        if j < -960:
            j = 960
            h2 = randint(-320, 0)

        #acrescenta o bg
        if k < -960:
            k = 960
            h3 = randint(-320, 0)

        if l < -960:
            l = 960
            h4 = randint(-320, 0)
            

            
        tela.blit(bg1, (int(i), h1))
        tela.blit(bg2, (int(j), h2))

        tela.blit(bg3, (int(k), h3))
        tela.blit(bg4, (int(l), h4))

        #atualiza a tela
        pygame.display.update()
        i-=1
        j-=1
        k-=2
        l-=2
        
    #pygame.quit()



#INSIDE OF THE GAME LOOP
#

#REST OF ITEMS ARE BLIT'D TO SCREEN.


main()
