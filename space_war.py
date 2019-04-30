import sys
import pygame
# from pygame.locals import *

from settings import Settings

def main():
    # Initialize the game
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Space War")

    # Main game loop
    while(True):
        # Keyboard and mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(game_settings.bg_color)

        # Draw the screen
        pygame.display.flip()

#call the "main" function if running this script
if __name__ == '__main__':
    main()