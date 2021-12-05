import pygame



class Display:

    def __init__(self, h, w, title):

        self.title = title
        self.width = w
        self.heigh = h
        
        self.display = pygame.display.set_mode([h, w])
        pygame.display.set_caption(title)

    def fill(self, color):
        self.display.fill(color)
        pass
##        pygame.display.set_caption("ola")
