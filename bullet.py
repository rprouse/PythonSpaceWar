import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A bullet fired from a player'''

    def __init__(self, settings, screen, player):
        '''Create a bullet at the player's current position'''
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        '''Update the position of the bullet'''
        self.y -= self.speed_factor
        self.rect.y = self.y

    def blitme(self):
        '''Draw the bullet'''
        pygame.draw.rect(self.screen, self.color, self.rect)
