from pygame import Surface
from pygame.sprite import Sprite
from configuration import Configuration

config = Configuration()

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = Surface([50,50])
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.jump_force = 0

    def update(self):
        self.vy += (config.gravity - self.jump_force)
        self.rect.y += self.vy
