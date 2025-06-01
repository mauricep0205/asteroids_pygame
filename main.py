import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # limit fps to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
