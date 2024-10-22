import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Start ship and configure origin of the ship"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Generate ship and create its rect.
        self.image = pygame.image.load('images/ship_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Initiate ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom        

        #Decimal value for ship's starting point
        self.center = float(self.rect.centerx)

        #Movement
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update ship coordinates using keyboard"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor


        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor


        self.rect.centerx = self.center        


    def blitme(self):
        """Generate ship and its location"""
        self.screen.blit(self.image, self.rect)