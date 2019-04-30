import sys
import pygame

def run_game():
    # Initialize the game
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Space War")

    # Main game loop
    while(True):
        # Keyboard and mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Draw the screen
        pygame.display.flip()

run_game()