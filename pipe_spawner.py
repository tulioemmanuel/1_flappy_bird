import random
from pygame import Surface
from pygame.sprite import Sprite,Group
from configuration import Configuration

config = Configuration()


class Pipe(Sprite):
    def __init__(self,flip):
        Sprite.__init__(self)
        self.image = Surface([config.pipe_width, config.max_pipe_height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = config.SCREEN_SIZE[0]
        
        offset = random.randint(10 , 500)

        self.rect.y = 0 - offset if not flip else config.SCREEN_SIZE[1] - self.rect.h + offset
        self.vx = 0
        self.vy = 0


class PipeSpawner(object):
    PIPE_MAX = 4
    MAX_DELTA = 1000
    PIPE_SPEED = 10

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
