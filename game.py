import pygame
from pygame.sprite import Group

from settings import Settings
from player import Player
from bullet import Bullet

class Game():
    '''Common game functions'''

    def __init__(self):
        '''Initialize the game'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space War")

        self.player = Player(self.screen, self.settings)
        self.bullets = Group()  # Player bullets


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
                elif event.key == pygame.K_SPACE and len(self.bullets) < self.settings.num_bullets:
                    self.bullets.add(Bullet(self.settings, self.screen, self.player))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.player.stop_moving()

        return True

    def update_screen(self):
        '''Draw all game elements on the screen'''
        self.screen.fill(self.settings.bg_color)
        self.bullets.update()

        # Remove bullets that have exited the screen
        for bullet in self.bullets.copy():
            if(bullet.rect.bottom < 0):
                self.bullets.remove(bullet)

        # Draw all bullets
        for bullet in self.bullets:
            bullet.blitme()

        self.player.blitme()

        # Draw the screen
        pygame.display.flip()
