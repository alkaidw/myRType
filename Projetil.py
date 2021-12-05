from pygame.sprite import Sprite
import Imagens

class Projetil (Sprite):
    def __init__(self, display, x, y):
        Sprite.__init__(self)
        self.display = display
        self.image = Imagens.laser
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 1
        
    def movimento (self):
        self.rect.x += self.vel

    def draw(self):
        self.display.blit(self.image, (self.rect.x, self.rect.y))
