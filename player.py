import pygame

class Player():
    '''Represents the player in the game'''

    def __init__(self, screen):
        '''Initializes the player and it's starting position'''
        self.screen = screen

        # Load the player image
        self.image = pygame.image.load('images/player.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''Draw the player at the current location'''
        self.screen.blit(self.image, self.rect)
