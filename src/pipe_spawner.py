import random
import pygame 
from pygame.sprite import Sprite,Group
from configuration import Configuration
from assets import Assets   

config = Configuration()


class Pipe(Sprite):
    def __init__(self,flip):
        Sprite.__init__(self)

        self.image = Assets().sprites['pipegreen']
        
        if not flip:
            self.image = pygame.transform.flip(self.image,False,True)

        self.rect = self.image.get_rect()
        self.rect.x = config.SCREEN_SIZE[0]
        
        offset = random.randint(10 , 200)

        self.rect.y = 0 - offset if not flip else config.SCREEN_SIZE[1] - self.rect.h + offset
        self.vx = 0
        self.vy = 0


class PipeSpawner(object):
    PIPE_MAX = config.pipe_max
    MAX_DELTA = config.pipe_delta
    PIPE_SPEED = config.pipe_speed

    def __init__(self):
        self.pipes = Group()
        self.current_delta = 0
        self.flip = False

    def update(self, delta):
        self.current_delta += delta
        if (
            self.current_delta >= PipeSpawner.MAX_DELTA
            and len(self.pipes) < PipeSpawner.PIPE_MAX
        ):
            self.spawn()
            self.current_delta = 0
            self.flip = not self.flip
        
        for pipe in self.pipes:
            pipe.rect.x -= PipeSpawner.PIPE_SPEED
            if pipe.rect.x + pipe.rect.w <= 0:
                self.pipes.remove(pipe)

    def spawn(self):
        self.pipes.add(Pipe(self.flip))

    def clean(self):
        self.pipes = Group()
        self.current_delta = 0
