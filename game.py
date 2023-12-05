from enum import Enum
import pygame
from configuration import Configuration
from player import Player
from pipe_spawner import PipeSpawner
from assets import Assets,ASSETS_DIR
from hud import HUD

config = Configuration()


class GameState(Enum):
    MENU = 1
    LOOP = 2
    PAUSED = 3
    STOPPED = 4


class Game(object):
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(config.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.running = False
        self.player = Player()
        self.pipe_spawner = PipeSpawner()
        self.assets = Assets()
        self.hud = HUD()
        self.delta = 0
        self.touched = False
        self.state = GameState.LOOP
        self.points = 0
        # self.state = GameState.MENU

    def setup(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.you_suck_text = self.font.render("YOU SUCK !", False, (255, 255, 255))
        self.start_text = self.font.render("START", False, (255, 255, 255))
        self.quit_text = self.font.render("QUIT", False, (255, 255, 255))
        self.bg_image1 = pygame.image.load(f"{ASSETS_DIR}\\sprites\\background-day.png")
        self.bg_image2 = pygame.image.load(f"{ASSETS_DIR}\\sprites\\background-day.png")
        self.bg_x = 0
        self.running = True

    def run(self):
        self.input()
        self.render()
        # if self.state == GameState.MENU:
        #     self.render_menu()
        # elif self.state == GameState.LOOP:
        #     if not self.touched:
        #         self.update(self.delta)
        #         self.render()

        pygame.display.flip()
        pygame.display.update()
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
                if self.state == GameState.MENU:
                    self.state = GameState.LOOP
                elif self.state == GameState.LOOP:
                    self.player.jump()
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                self.player.jump_force = 0
                self.player.current_sprite = 2

    def update(self, delta):
        self.player.update()
        self.pipe_spawner.update(delta)
        self.check_collision()

    def render_menu(self):
        self.screen.blit(
            self.start_text,
            (
                self.screen.get_rect().w / 2 - self.start_text.get_rect().w / 2,
                self.screen.get_rect().h / 2,
            ),
        )
        self.screen.blit(
            self.quit_text,
            (
                self.screen.get_rect().w / 2 - self.quit_text.get_rect().w / 2,
                self.screen.get_rect().h / 2 + 100,
            ),
        )
    
    def draw_bg(self):
        self.screen.blit(self.bg_image1,(self.bg_x,0))
        self.screen.blit(self.bg_image2,(self.bg_image1.get_width() + self.bg_x , 0 ))
        self.bg_x -= 1
        if self.bg_x < -self.bg_image1.get_width():
            self.bg_x = 0


    def render(self):
        self.screen.fill((0, 0, 0))
        # self.draw_bg() # chamar UI no objeto principal

        img = pygame.image.load("1.png")
        self.screen.blit(img, (100,100))
        img = pygame.image.load("src/1.png")
        self.screen.blit(img, (0,0))

        # self.pipe_spawner.pipes.draw(self.screen)
        # self.screen.blit(self.player.image, self.player.rect)
        # if self.touched:
        #     self.screen.blit(
        #         self.you_suck_text,
        #         (
        #             self.screen.get_rect().w / 2 - self.you_suck_text.get_rect().w / 2,
        #             self.screen.get_rect().h / 2,
        #         ),
        #     )
        # self.hud.draw(self.screen,self.points) # ou criar um objeto de UI e ter uma lógica apartada

    def check_collision(self):
        if self.player.rect.y - self.player.rect.h >= self.screen.get_rect().h:
            self.touched = True

        if pygame.sprite.spritecollide(self.player, self.pipe_spawner.pipes, False):
            self.touched = True

        for pipe in self.pipe_spawner.pipes:
            if pipe.rect.x == self.player.image.get_rect().x:
                self.points += 1
