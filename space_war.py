import sys
import pygame
# from pygame.locals import *

from game import Game

def main():
    # Initialize the game
    game = Game()

    # Main game loop
    while(True):
        # Keyboard and mouse input
        if game.process_input() == False:
            return  # Game over

        game.update_screen()

#call the "main" function if running this script
if __name__ == '__main__':
    main()