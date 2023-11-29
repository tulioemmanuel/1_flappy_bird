import os
import pygame

ASSETS_DIR = os.getcwd() + "\\src\\assets"


class AssetsMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Assets(metaclass=AssetsMeta):
    def __init__(self) -> None:
        self.sprites = {"bluebird": [], "redbird": [], "yellowbird": []}
        self.load_assets()

    def load_assets(self):
        self.sprites.get("bluebird").append(
            pygame.image.load(f"{ASSETS_DIR}\\sprites\\bluebird-downflap.png")
        )
        self.sprites.get("bluebird").append(
            pygame.image.load(f"{ASSETS_DIR}\\sprites\\bluebird-midflap.png")
        )
        self.sprites.get("bluebird").append(
            pygame.image.load(f"{ASSETS_DIR}\\sprites\\bluebird-upflap.png")
        )

        self.sprites.get("redbird").append(
            pygame.image.load(f"{ASSETS_DIR}\\sprites\\redbird-downflap.png")
        )
        self.sprites.get("redbird").append(
            pygame.image.load(f"{ASSETS_DIR}\\sprites\\redbird-midflap.png")
        )
        self.sprites.get("redbird").append(
            pygame.image.load(f"{ASSETS_DIR}\\sprites\\redbird-upflap.png")
        )

        self.sprites.get("yellowbird").append(
            pygame.image.load(f"{ASSETS_DIR}\\sprites\\yellowbird-downflap.png")
        )
        self.sprites.get("yellowbird").append(
            pygame.image.load(f"{ASSETS_DIR}\\sprites\\yellowbird-midflap.png")
        )
        self.sprites.get("yellowbird").append(
            pygame.image.load(f"{ASSETS_DIR}\\sprites\\yellowbird-upflap.png")
        )

        self.sprites['pipegreen'] = pygame.image.load(f"{ASSETS_DIR}\\sprites\\pipe-green.png")
        self.sprites['pipered'] = pygame.image.load(f"{ASSETS_DIR}\\sprites\\pipe-red.png")
        self.sprites['backgroundday'] = pygame.image.load(f"{ASSETS_DIR}\\sprites\\background-day.png")
