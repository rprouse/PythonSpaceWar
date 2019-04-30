import sys
import pygame
# from pygame.locals import *

def main():
    # Initialize the game
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Space War")

    bg_color = (10, 30, 60)

    # Main game loop
    while(True):
        # Keyboard and mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(bg_color)

        # Draw the screen
        pygame.display.flip()

#call the "main" function if running this script
if __name__ == '__main__':
    main()