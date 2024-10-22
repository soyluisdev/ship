import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initiate pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Background color
    bg_color = (230, 230, 230)
    ship = Ship(ai_settings, screen)

    #Start main loop
    while True:
        
        #Capture keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
        #Change screen color through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #Generate screen
        pygame.display.flip()

run_game()