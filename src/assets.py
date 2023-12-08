import sys
import os
import pygame

ASSETS_DIR = (
    os.path.join(os.getcwd(), "assets")
    if sys.platform == "emscripten"
    else os.path.join(os.getcwd(), "src", "assets")
)


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
            pygame.image.load(
                os.path.join(ASSETS_DIR, "sprites", "bluebird-downflap.png")
            )
        )
        self.sprites.get("bluebird").append(
            pygame.image.load(
                os.path.join(ASSETS_DIR, "sprites", "bluebird-midflap.png")
            )
        )
        self.sprites.get("bluebird").append(
            pygame.image.load(
                os.path.join(ASSETS_DIR, "sprites", "bluebird-upflap.png")
            )
        )

        self.sprites.get("redbird").append(
            pygame.image.load(
                os.path.join(ASSETS_DIR, "sprites", "redbird-downflap.png")
            )
        )
        self.sprites.get("redbird").append(
            pygame.image.load(
                os.path.join(ASSETS_DIR, "sprites", "redbird-midflap.png")
            )
        )
        self.sprites.get("redbird").append(
            pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "redbird-upflap.png"))
        )

        self.sprites.get("yellowbird").append(
            pygame.image.load(
                os.path.join(ASSETS_DIR, "sprites", "yellowbird-downflap.png")
            )
        )
        self.sprites.get("yellowbird").append(
            pygame.image.load(
                os.path.join(ASSETS_DIR, "sprites", "yellowbird-midflap.png")
            )
        )
        self.sprites.get("yellowbird").append(
            pygame.image.load(
                os.path.join(ASSETS_DIR, "sprites", "yellowbird-upflap.png")
            )
        )

        self.sprites["pipegreen"] = pygame.image.load(
            os.path.join(ASSETS_DIR, "sprites", "pipe-green.png")
        )
        self.sprites["pipered"] = pygame.image.load(
            os.path.join(ASSETS_DIR, "sprites", "pipe-red.png")
        )
        self.sprites["backgroundday"] = pygame.image.load(
            os.path.join(ASSETS_DIR, "sprites", "background-day.png")
        )

        self.sprites["menu"] = pygame.image.load(
            os.path.join(ASSETS_DIR, "sprites", "message.png")
        )   

        self.sprites["gameover"] = pygame.image.load(
            os.path.join(ASSETS_DIR, "sprites", "gameover.png")
        )   

        self.sprites["floor"] = pygame.image.load(
            os.path.join(ASSETS_DIR, "sprites", "base.png")
        )   

        self.sprites["numbers"] = {
            "0": pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "0.png")),
            "1": pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "1.png")),
            "2": pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "2.png")),
            "3": pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "3.png")),
            "4": pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "4.png")),
            "5": pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "5.png")),
            "6": pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "6.png")),
            "7": pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "7.png")),
            "8": pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "8.png")),
            "9": pygame.image.load(os.path.join(ASSETS_DIR, "sprites", "9.png")),
        }
