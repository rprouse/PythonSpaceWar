import pygame

from settings import Settings
from player import Player

class Game():
    '''Common game functions'''

    def __init__(self):
        '''Initialize the game'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space War")

        self.player = Player(self.screen, self.settings)


    def process_input(self):
        '''Process keyboard and mouse input'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.move_left()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.player.stop_moving()

        return True

    def update_screen(self):
        '''Draw all game elements on the screen'''
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()

        # Draw the screen
        pygame.display.flip()
