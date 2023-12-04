import pygame, sys

#Fixed variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
FRAMERATE = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# With this, we fix that the game speed is the same for every computer (does not depend on hardware)
clock = pygame.time.Clock()

#test_surface = pygame.Surface((100,200))
#test_surface.fill((0,0,255))
#x_pos = 200
#test_rect = pygame.Rect(100, 200, 100, 100)   # Rectangle allows me to have a different control than the surface! Less code
#test_rect = test_surface.get_rect(center = (200, 250))      # Gets the surface and puts a rectangle around it

while True:
    
    # Search for events
    for event in pygame.event.get():
        
        # Search for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Draw all our elements
    screen.fill((175, 215, 70))
    
    #test_rect.right += 1
    #pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    #x_pos -= 1
    #screen.blit(test_surface, (x_pos, 250))
    #screen.blit(test_surface, test_rect)   # blit -> block image transfer      //      position is in the top left corner of the surface
    
    pygame.display.update()
    clock.tick(FRAMERATE)