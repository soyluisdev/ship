import sys
import pygame

def run_game():
    #Initiate screen of the project
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #Background color
    bg_color = (230, 230, 230)

    #Start main loop
    while True:
        
        #Capture keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Change screen color through the loop
        screen.fill(bg_color)

        #Generate screen
        pygame.display.flip()

run_game()