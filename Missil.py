from pygame.sprite import Sprite
import Imagens

class Missil (Sprite):
    def __init__(self, display, x, y):
        Sprite.__init__(self)
        self.display = display
        self.image = Imagens.missil
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velx = 1
        self.vely = 1
        
    def movimento (self):
        self.rect.x += self.velx
        self.rect.y += self.vely

    def draw(self):
        self.display.blit(self.image, (self.rect.x, self.rect.y))
