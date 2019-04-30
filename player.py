import pygame

class Player():
    '''Represents the player in the game'''

    def __init__(self, screen):
        '''Initializes the player and it's starting position'''
        self.screen = screen

        # Load the player image
        image = pygame.image.load('images/player.bmp')
        rect = image.get_rect()
        self.image = pygame.transform.scale(image, (rect.width * 4, rect.height * 4))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.moving_left = False
        self.moving_right = False

        # Start at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

    def move_right(self):
        self.moving_right = True

    def move_left(self):
        self.moving_left = True

    def stop_moving(self):
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        '''Draw the player at the current location'''
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1

        self.screen.blit(self.image, self.rect)
