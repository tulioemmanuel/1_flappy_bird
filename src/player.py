from pygame import Surface
from pygame.sprite import Sprite
from configuration import Configuration
from assets import Assets

config = Configuration()

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.jump_force = 0
        self.current_sprite = 0
        self.sprites = Assets().sprites.get('bluebird')
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

    def update(self):
        self.vy += (config.gravity - self.jump_force)
        self.rect.y += self.vy
        self.image = self.sprites[self.current_sprite]
        
        if self.current_sprite == 2:
            self.current_sprite = 0

        
