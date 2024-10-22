import sys
import pygame

def check_events():
    """Mouse and keyboard events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update all the screen events and change of screen"""
    #Generate the new screen for each pass of the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Load the most recent screen
    pygame.display.flip()


def check_events(ship):
    """Connect keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False