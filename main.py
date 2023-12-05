import asyncio
from game import Game

async def main():
    flappy_bird = Game()
    flappy_bird.setup()
    while flappy_bird.running:
        flappy_bird.run()
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())


