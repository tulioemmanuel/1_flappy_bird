import pygame
from configuration import Configuration
from player import Player
from pipe_spawner import PipeSpawner

config = Configuration()

class Game(object):
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(config.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.running = False
        self.player = Player()
        self.pipe_spawner = PipeSpawner()
        self.delta = 0

    def setup(self):
        pygame.init()
        self.running = True

    def run(self):
        self.input()
        self.update(self.delta)
        self.render()
        self.delta = self.clock.tick(config.FPS)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_LCTRL:
                    self.player.jump_force = config.jump_force
            elif event.type == pygame.KEYUP:                                    
                if event.key == pygame.K_LCTRL:
                    self.player.jump_force = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.jump_force = config.jump_force
            elif event.type == pygame.MOUSEBUTTONUP:
                self.player.jump_force = 0
                

    def update(self,delta):
        self.player.update()
        self.pipe_spawner.update(delta)

    def render(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.player.image, self.player.rect)
        self.pipe_spawner.pipes.draw(self.screen)
        pygame.display.flip()
        pygame.display.update()

