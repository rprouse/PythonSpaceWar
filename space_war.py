import sys
import pygame
# from pygame.locals import *

from settings import Settings
from player import Player

def main():
    # Initialize the game
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Space War")

    player = Player(screen)

    # Main game loop
    while(True):
        # Keyboard and mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(game_settings.bg_color)
        player.blitme()

        # Draw the screen
        pygame.display.flip()

#call the "main" function if running this script
if __name__ == '__main__':
    main()