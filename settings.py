class Settings():
    '''A class to store settings for the game'''

    def __init__(self):
        '''Initialize the game's settings'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.player_speed = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 128, 0)

