import pygame
from assets import Assets

OFFSET_X = 30
OFFSET_Y = 10

class HUD(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.numbers = Assets().sprites["numbers"]

    def draw(self, screen,points):
        numbers = []
        while points // 10 != 0:
            numbers.insert(0,points % 10)
            points = points//10
        for i,n in enumerate(numbers):            
            screen.blit(self.numbers[str(n)], (self.numbers[str(n)].get_rect().w * i , OFFSET_Y))

