class Settings():
    """This class stores all the settings for alien invasion file"""

    def __init__(self):
        """Game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

        #Bullets
        self.bullet_speed_factor = 1
        self.bullet_witdh = 3
        self.bullet_height = 15
        self.bullet_color = 70,70,70
        